# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/<operation>')
def math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    if operation == 'add':
        return str(add(a, b))
    if operation == 'sub':
        return str(sub(a, b))
    if operation == 'mult':
        return str(mult(a, b))
    if operation == 'div':
        return str(div(a, b))


@app.route('/math/<operation>')
def better_math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    operators = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }

    return str(operators[operation](a, b))
