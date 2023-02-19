from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return 'welcome'


@app.route('/welcome/<location>')
def welcome_loc(location):
    return f'welcome {location}'
