from diagrams import Cluster, Diagram
from diagrams.onprem.analytics import Hadoop
from diagrams.onprem.inmemory import Memcached
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.logging import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

with Diagram("Bloosa architecture", show=False):
    nginx = Nginx("nginx")

    metrics = Prometheus("metric")
    metrics << Grafana("monitoring")

    with Cluster("Apps Cluster"):
        grpcsvc = [
            Server("puma 1"),
            Server("puma 2"),
            Server("puma 3")]

    cache = Memcached('Cache')
    grpcsvc >> cache

    with Cluster("Sessions HA"):
        master = Redis("session")
        master - Redis("replica") << metrics
        grpcsvc >> master

    with Cluster("Database HA"):
        master = PostgreSQL("users")
        master - PostgreSQL("slave") << metrics
        grpcsvc >> master

    aggregator = Fluentd("logging")
    # aggregator >> Kafka("stream") >> Hadoop("analytics")
    aggregator >> Hadoop("analytics")

    nginx >> grpcsvc >> aggregator
    nginx >> cache
    cache >> nginx
