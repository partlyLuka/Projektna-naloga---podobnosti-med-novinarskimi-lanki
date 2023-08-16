#siol_dobi_url

import os 
import validators
import requests
import traceback
import time
#from selenium import webdriver
import re 
import json
import datetime
#zbrali bomo linke zadnjega leta.

#seznam datumov nam bo prišel prav:
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(365)]
dates = [(x.year, x.month, x.day) for x in date_list]

urlji_arhiva = [f'https://siol.net/pregled-dneva/{x[0]}-{x[1]}-{x[2]}/' for x in dates ]
arhiv_directory_SIOL = "arhiv_SIOL"
def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
        page_content = requests.get(url)
        if page_content.status_code == 200:
            return page_content.text
        else:
            raise ValueError(f"Čudna koda: {page_content.status_code}")
    except Exception:
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print(f"Prišlo je do spodnje napake:\n{traceback.format_exc()}")
       
def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None
#shranimo vsebina strani arhiva
def save_frontpage(page, directory, filename):
    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
    "directory"/"filename"."""
    html_strani = download_url_to_string(page)
    save_string_to_file(html_strani, directory, filename)
#save_frontpage('https://siol.net/pregled-dneva/2023-3-9/', arhiv_directory_SIOL, "test")
vz = r'<article class="card card--timemachine cf">.+?<a title="(?P<naslov>.+?)" href="(?P<link>.+?)" class'
tekst = download_url_to_string('https://siol.net/pregled-dneva/2023-3-9/')
clanki = {}
#for najdba in re.finditer(v, tekst, flags=re.DOTALL):
#    naslov = najdba["naslov"]
#    link = 'https://siol.net' + najdba["link"]
#    clanki[naslov] = {}
#    clanki[naslov]["link"] = link

def nalozi_vec_html():
    i = 0 
    for page in urlji_arhiva:
        i += 1 
        print(f"{i} of {len(dates)}")
        save_frontpage(page, arhiv_directory_SIOL, f'arhiv_html_siol{i}')
        time.sleep(1)    
nalozi_vec_html()
def dobi_naslov_url(vhod):
    with open(vhod, "r", encoding='utf-8') as v:
        tekst = v.read()
        for najdba in re.finditer(vz, tekst, flags=re.DOTALL):
            naslov = najdba["naslov"]
            link = 'https://siol.net' + najdba["link"]
            clanki[naslov] = {}
            clanki[naslov]["link"] = link

os.chdir("arhiv_SIOL")
def dobi_vec_naslov_url():
    for file in os.listdir():
        print(file)
        dobi_naslov_url(file)

dobi_vec_naslov_url()
def preveri_ali_so_url_ok():
    i = 0
    for k in clanki:
        link = clanki[k]["link"]
        a = validators.url(link) 
        if not a:
            i += 1
    print(f"{i} linkov ni ok") 
preveri_ali_so_url_ok() 
print(len(clanki))
os.chdir("..")
with open("JSON_SIOL1.json", "w", encoding='utf-8') as d:
    json.dump(clanki, d)