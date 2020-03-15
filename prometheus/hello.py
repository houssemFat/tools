from prometheus_client import start_http_server, Summary, Histogram, Counter, Gauge
import random
import time

# Create a metric to track time spent and requests made.
request_time = Summary('request_processing_seconds', 'Time spent processing request')
histogram = Histogram('request_latency_seconds', 'Request latency')
#histogram.DEFAULT_BUCKETS = (.005, .01, .025, .05, .075, .1, .25, .5, .75, 1.0, 2.5, 5.0, 7.5, 10.0, INF)
counter = Counter(
    'http_requests_total', 'Total Request Count'
)
in_progress = Gauge(
    'requests_in_progress_total', 'Requests in progress'
)


# Decorate function with metric.
@request_time.time()
@histogram.time()
#@in_progress.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)
    time.sleep(2)
    #counter.inc()


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(4000)
    # Generate some requests.
    while True:
        process_request(random.random())
