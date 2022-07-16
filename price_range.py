# Checking a price range in shop for a intel CPUs

from bs4 import BeautifulSoup
import requests
inp = input("Do you want to search for a AMD or Intel CPUS? ")
if (inp.lower() == "amd"):
    cpu = "amd"
elif (inp.lower() == "intel"):
    cpu = "intel"
else:
    print("You gave wrong value")
    
url = f"https://www.komputronik.pl/search-filter/401/procesory-{cpu}"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
ul = doc.find("ul", class_ = "product-entry2-wrap")
for li in ul.find_all("li", class_ = "product-entry2"):
    cena = list(li.find("span", class_ = "price").contents[1].strings)
    nazwa = li.find("div", class_= "inline-features").string
    proc = li.find("div", class_ = "pe2-head").contents[1].string.strip()
    if (proc == "POLECANE"): proc = li.find("div", class_ = "pe2-head").contents[3].string.strip()
    podzial = nazwa.strip().split("|")
    details = list(li.find("ul", class_ = "key-features2 pe2-desc").contents)
    cores = details[7].contents[1].string.strip().split(" ")
    mhz = details[9].contents[1].string.strip()
    tmhz = details[11].contents[1].string.strip()

    wynik = f"""{proc} 
{cores[0]} Cores | {mhz} - {tmhz}
{cena[0].strip()} {cena[1]}
"""
        
    
    print(wynik)

    
    
