import json
from flask import Flask, request, Response



app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello world"


@app.route("/method", methods=["GET", "POST", "PUT", "DELETE"])
def methods():
    return request.method


@app.route("/status-code/<int:status_code>/")
def status_code(status_code):
    return "status{}".format(status_code), status_code


@app.route("/", methods=["POST"])
def post_data():
    return json.dumps(request.form)


@app.route("/data", methods=["POST"])
def data():
    print(request.data)
    return json.dumps(request.data.decode())


@app.route("/plain-response")
def plain_response():
    return Response(
        "{'response': 'Hello World'}",
        status=200,
        headers=dict(),
        content_type="application/javascript"
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000
    )

