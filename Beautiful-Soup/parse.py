import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

r = requests.get("https://projecteuler.net/archives")
soup = BeautifulSoup(r.text, 'html.parser')

liste = []

for row in soup.find_all("tr"):
    col = row.find_all("td")
    if col != []:
        n = {
            "sira_no"  : col[0].string,
            "name"     : col[1].string,
            "solved"   : col[2].string
        }
        liste.append(n)

with open("scrap_veri.json", "w") as f:
    json.dump(liste, f)
    print("File is created.")