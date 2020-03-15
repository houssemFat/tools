from flask import Flask, jsonify  # import main Flask class and request object

app = Flask(__name__)  # create the Flask app


@app.route('/alert-manager-web-hooks', methods=['GET', 'POST'])
def webhooks():
    print('An alert is fired')
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # run app in debug mode on port 5000
