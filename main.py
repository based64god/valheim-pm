#!/usr/bin/env python3
import flask
import click
import json
import os

secret=os.getenv('SECRET')

app = flask.Flask(__name__)

@click.command()
@click.option('--package-dir', default=os.getcwd(), prompt='system path to package dir', 
    help='an absolute path to where your valheim packages should be installed')

@app.route("/")        # Standard Flask endpoint
def run_github_webhook():
    data = json.loads(flask.request.get_json())
    print(flask.request.data)
    print(data)
    return



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

