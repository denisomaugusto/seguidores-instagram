import requests
import re

URL = "https://www.instagram.com/tsukipersonalizados/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=20)

if response.status_code == 200:
    html = response.text
    match = re.search(r'"edge_followed_by":{"count":(\d+)}', html)

    if match:
        seguidores = match.group(1)
        with open("seguidores.txt", "w") as f:
            f.write(seguidores)
