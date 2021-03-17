#!/usr/bin/env python3
from flask import Flask, request
from pathlib import Path
import requests
import click
import json
import os
from apscheduler.schedulers.background import BackgroundScheduler




@click.command()
@click.option('--package-dir', '-p', default=os.getcwd(), prompt='system path to package dir', 
    help='an absolute path to where your valheim packages should be installed')
@click.option('--download-urls', '-u', multiple=True, prompt='the download urls for your valheim dlls',
    help='references to binary locations on the internet')
@click.option('--use-webhooks/--no-webhooks', default=False, prompt='use webhooks to update packages. ignores -d -h -m -s.')
@click.option('--days', '-d', default=0, prompt='length in days for how long download jobs should wait')
@click.option('--hours', '-h', default=1, prompt='length in hours for how long download jobs should wait')
@click.option('--minutes', '-m' default=0, prompt='length in minutes for how long download jobs should wait')
@click.option('--seconds', '-s', default=0, prompt='length in seconds for how long download jobs should wait')

def download_job():
    for i, url in enumerate(urls):
        r = requests.get(url)
        with open(Path(package_path / str(i) + ".dll" ), 'wb') as f:
            f.write(r.content)



@app.route("/", methods=['POST'])        # Standard Flask endpoint
def run_github_webhook():
    parsed = json.loads(request.data)
    url = parsed['repository']['clone_url']
    owner = parsed['repository']['owner']['name']
    name = parse['repository']['owner']['name']
    if not package_path.is_dir():
        return None
    # TODO: finish this
    return 'ok'



if __name__ == "__main__":
    package_path = Path(package_dir)
    package_path.mkdir(parents=True, exist_ok=True)
    print("Creating package dir if it doesn't already exist")
    urls = download_urls
    if use_webhooks:
        secret=os.getenv('SECRET')
        app = Flask(__name__)
        app.run(host="0.0.0.0", port=8080)
    else:
        sched = BackgroundScheduler()
        sched.add_job(download_job, 'interval', days=days, hours=hours, minutes=minutes, seconds=seconds)
        sched.start()