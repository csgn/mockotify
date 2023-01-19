import sys

from flask import Flask, request

import producer

p = producer.Producer()

app = Flask(__name__)



@app.route("/")
def index():
    return ":)"

@app.route("/recommend", methods=["GET"])
def recommend():
    message = request.args.get("refer_id")

    p.send(message)

    return ":"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
