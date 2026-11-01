import time

import requests
from flask import Flask, request

app = Flask(__name__)
FLUENTD = "http://localhost:8080"
count = 0


@app.route("/log")
def log():
    global count
    start = time.time()
    count += 1
    query = request.args.get("query", "")
    requests.post(FLUENTD + "/myapp.log", json={"query": query})
    requests.post(FLUENTD + "/myapp.metrics", json={
        "requests_total": count,
        "duration_ms": (time.time() - start) * 1000,
    })
    return "ok"


app.run(port=5000)
