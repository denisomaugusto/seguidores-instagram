import requests
import json
import sys

URL = "https://api.allorigins.win/raw?url=https://socialblade.com/instagram/user/tsukipersonalizados"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def main():
    try:
        r = requests.get(URL, headers=headers, timeout=20)
        if r.status_code != 200:
            return

        html = r.text

        import re
        match = re.search(r'Followers<\/span>\s*<span[^>]*>([\d,]+)', html)

        if not match:
            return

        seguidores = match.group(1).replace(",", "")

        with open("seguidores.txt", "w") as f:
            f.write(seguidores)

        print("Atualizado:", seguidores)

    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
    sys.exit(0)
