from typing import Dict, Tuple, Union

from flask import Flask, request


app = Flask(__name__)


ErrorResponse = Tuple[Dict[str, Union[str, int]], int]
MathResponse = Dict[str, float]


def error(code: int, message: str) -> ErrorResponse:
    _err = {"error_code": code, "error": message}
    return _err, code


@app.route("/")
@app.route("/greeting")
def greet() -> Dict[str, str]:
    _response = {"greeting": "Hello, world!"}
    return _response


@app.route("/greeting/<user>")
def greet_user(user: str) -> Dict[str, str]:
    _response = {"greeting": "Hello", "user": user}
    return _response


@app.route("/math/sum", methods=["POST"])
def add_by_api() -> Union[MathResponse, ErrorResponse]:
    _to_add = request.form.getlist("add")
    if _to_add is not None:
        _sum = sum(float(n) for n in _to_add)
        return {"sum": _sum}
    else:
        return error(400, 'Bad request: "add" not present in request body')
