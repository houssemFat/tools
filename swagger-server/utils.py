import yaml
from os import path

_gets = {}
_posts = {}
_puts = {}
_batchs = {}


def read_swagger_file():
    current_dir = path.dirname(path.realpath(__file__))
    with open(path.join(current_dir, 'tree.yml')) as f:
        # use safe_load instead load
        dataMap = yaml.safe_load(f)

    for _path in dataMap['paths']:
        _info = dataMap['paths'][_path]
        if 'get' in _info:
            _gets[_path]= _info
        if 'post' in _path:
            _gets[_path]= _info

    print(_gets)


def parse_path(route):

