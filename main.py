#!/usr/bin/env python3
import flask
import click
import os

secret=os.getenv('SECRET')

app = flask.Flask(__name__)

@click.command()
@click.option('--package-dir', default=os.getcwd(), prompt='system path to package dir', 
    help='an absolute path to where your valheim packages should be installed')

@app.route('/payload', methods=['POST'])
def run_github_webhook(package_dir):
    json = request.json()
    if json is None:
        print('failed on request': request)
        return
    print('i got json:', json)
    
