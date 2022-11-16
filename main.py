from flask import Flask, render_template
from markupsafe import escape

from apicalls import *

app = Flask(__name__)


@app.route('/')
def index():
    result = []
    for i in GetFlows()['value']:
        result.append({'name': i['crea7_name'],
                      'value': GetValues(i['crea7_name'])})
    return render_template('index.html', num=result)


# @app.route('/<company>/home')
# def index(company):
    # return render_template('index.html', company=company)


# @app.route('/<company>/dashboard')
# def index(company):
    # return render_template('index.html', company=company)


# @app.route('/<company>/automations/')
# def index(company):
    # return render_template('index.html', company=company)
