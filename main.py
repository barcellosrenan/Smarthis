from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/<company>/home')
# def index(company):
    # return render_template('index.html', company=company)


# @app.route('/<company>/dashboard')
# def index(company):
    # return render_template('index.html', company=company)


# @app.route('/<company>/automations/')
# def index(company):
    # return render_template('index.html', company=company)
