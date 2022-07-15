# Checking a price range in shop for a intel CPUs

from bs4 import BeautifulSoup
import requests

url = "https://www.komputronik.pl/category/401/procesory.html"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
ul = doc.find("ul", class_ = "product-entry2-wrap")
for li in ul.find_all("li", class_ = "product-entry2"):
    cena = list(li.find("span", class_ = "price").contents[1].strings)
    nazwa = li.find("div", class_= "inline-features").string
    podzial = nazwa.strip().split("|")
    wynik = f"{podzial[0]}/{podzial[1]}/{podzial[2]} {cena[0].strip()} {cena[1]}"
    print(wynik)

    
    
