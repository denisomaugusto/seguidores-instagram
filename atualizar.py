import requests
import re
import sys

URL = "https://www.countik.com/instagram-username/tsukipersonalizados"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def main():
    try:
        r = requests.get(URL, headers=headers, timeout=20)

        if r.status_code != 200:
            print("HTTP error:", r.status_code)
            return

        html = r.text

        # tenta encontrar seguidores
        match = re.search(r'Followers</div><div[^>]*>([\d,.]+)', html)

        if not match:
            print("Seguidores não encontrados")
            return

        seguidores = match.group(1)
        seguidores = seguidores.replace(".", "").replace(",", "")

        if not seguidores.isdigit():
            print("Valor inválido:", seguidores)
            return

        with open("seguidores.txt", "w") as f:
            f.write(seguidores)

        print("Seguidores atualizados:", seguidores)

    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
    sys.exit(0)  # <- GARANTE QUE O WORKFLOW NÃO QUEBRE
