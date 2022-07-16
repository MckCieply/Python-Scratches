# Checking a price range in shop for a intel CPUs

from bs4 import BeautifulSoup
import requests
inp = input("Do you want to search for a AMD or Intel CPUS? ")
first_page = 1
if (inp.lower() == "amd"):
    cpu = 51
    last_page = 2
elif (inp.lower() == "intel"):
    cpu = 4
    last_page = 4
else:
    print("You gave wrong value")  
page = 1
for page in range(first_page, last_page+1):
    print(f"PAGE {page} \n")
    url = f"https://www.komputronik.pl/category/401/procesory.html?prod%5B%5D={cpu}&filter=1&showBuyActiveOnly=1&p={page}"
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
        try:
            tmhz = details[11].contents[1].string.strip()
        except: pass

        wynik = f"""{proc} 
    {cores[0]} Cores | {mhz} - {tmhz}
    {cena[0].strip()} {cena[1]}
    """
            
        
        print(wynik)
    page += 1

    
    
