#!/usr/bin/env python3
from flask import Flask, request
import click
import json
import os

secret=os.getenv('SECRET')

app = Flask(__name__)

@click.command()
@click.option('--package-dir', default=os.getcwd(), prompt='system path to package dir', 
    help='an absolute path to where your valheim packages should be installed')

@app.route("/", methods=['POST'])        # Standard Flask endpoint
def run_github_webhook():
    print(request.data)
    return 'ok'



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
