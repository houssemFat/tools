from flask import Flask, request, jsonify
# https://www.jetbrains.com/help/pycharm/configuring-folders-within-a-content-root.html
from utils import read_swagger_file, parse_path

read_swagger_file()

app = Flask(__name__)


@app.before_request
def parse_request():
    parse_path("/users")
    return jsonify({1: 3})


if __name__ == '__main__':
    app.run(debug=True)
