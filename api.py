import sys
import json

from flask import Flask, request

import producer
from cs import session

p = producer.Producer()

app = Flask(__name__)



@app.route("/")
def index():
    return ":)"

@app.route("/recommend", methods=["GET"])
def recommend():
    message = request.args.get("refer_id")

    p.send(message)

    return "OK"

@app.route("/suggests", methods=["GET"], defaults={"refer_id": None})
@app.route("/suggests/<refer_id>", methods=["GET"])
def suggests(refer_id=None):
    data = None

    if refer_id:
        data = session.execute(f"""
                SELECT JSON * from suggest
                WHERE refer_id = '{refer_id}'
            """)
    else:
        data = session.execute(f"""
                SELECT JSON * from suggest
        """)
    
    return [json.loads(i.json) for i in data]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
