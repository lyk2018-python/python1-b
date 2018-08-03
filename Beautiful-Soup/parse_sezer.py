from bs4 import BeautifulSoup
import requests
import json

r = requests.get("http://sezerbozkir.com/")
soup = BeautifulSoup(r.text, "html.parser")

liste = []

articles = soup.find_all("article")
for art in articles:
    liste.append(art.header.h1.a.string)

with open("sezer.json", "w", encoding="utf-8") as f:
    json.dump(liste, f, ensure_ascii=False)
    print("Dosya yazma başarılı.")