# backend/app.py

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/index')
def index():
    return "This is the index page of the Webbased Tester."


@app.route('/')
def home():
    name = request.args.get('name', 'Guest')
    return f"Welcome to the Webbased Tester, {escape(name)}!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
