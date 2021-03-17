#!/usr/bin/env python3
import flask
import click
import os
from github_webhook import Webhook

secret=os.getenv('SECRET')

app = flask.Flask(__name__)
webhook=Webhook(app)

@click.command()
@click.option('--package-dir', default=os.getcwd(), prompt='system path to package dir', 
    help='an absolute path to where your valheim packages should be installed')

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

