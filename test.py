import requests
import os
from pathlib import Path

print('Beginning file download with requests')

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
r = requests.get(url)
package_path = Path(os.getcwd())
package_path.mkdir(parents=True, exist_ok=True)
print("Creating package dir if it doesn't already exist")
with open(Path(package_path / 'testing.jpg'), 'wb') as f:
    f.write(r.content) 