"""HTTP-обёртка над калькулятором: GET /calc?op=add&a=2&b=3 -> {"result": 5}."""
from flask import Flask, jsonify, request

import calculator

app = Flask(__name__)

OPS = {
    "add": calculator.add,
    "sub": calculator.sub,
    "mul": calculator.mul,
    "div": calculator.div,
}


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/calc")
def calc():
    op = request.args.get("op", "add")
    if op not in OPS:
        return jsonify(error=f"unknown op: {op}"), 400
    try:
        a = float(request.args["a"])
        b = float(request.args["b"])
        return jsonify(result=OPS[op](a, b))
    except (KeyError, ValueError) as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
