#dobi_url_clankov

import os 
import requests
import traceback
import time
from selenium import webdriver
import re 
import json
browser = webdriver.Firefox()
#najprej bomo nalozili url strani arhivov clankov in iz te strani izluscili urlje do dejanskih clankov

#dobima html strani arhiva:
start = time.time()
#najprej definirajmo url, direktorij in mapo, kamor bomo shranili urlje od arhiva RTV, 24ur in Siol. Ustvarili smo mapo 'arhivi', kamor bomo shranili tri mape, napolnjeno s html-ji arhivov vsakega medija.
#arhiv za zadnje leto dni:
i_slo = 250
i_svet = 276
i_sport = 323
i_kultura = 213
i_zabava = 199
s = i_slo + i_svet + i_sport + i_kultura + i_zabava 

urlji_arhiva_RTV = {"slo" : [f"https://www.rtvslo.si/slovenija/arhiv/?&page={i}" for i in range(1, i_slo + 1)], 
                    "svet": [f"https://www.rtvslo.si/svet/arhiv/?&page={i}" for i in range(1, i_svet + 1)],
                    "sport": [f"https://www.rtvslo.si/sport/arhiv/?&page={i}" for i in range(1, i_sport + 1)], 
                    "kultura":[f"https://www.rtvslo.si/kultura/arhiv/?&page={i}" for i in range(1, i_kultura + 1)],
                    "zabava" : [f"https://www.rtvslo.si/zabava-in-slog/arhiv/?&page={i}" for i in range(1, i_zabava + 1)]}

arhiv_directory_RTV = "arhiv_RTV"
ime_datotek_htmljev_RTV = [f"RTV_stran_arhiva_{i}" for i in range(1,s + 1)]



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

#ti dve for zanki ne delujeta zaradi različnih razlogov (24 ur nima ok hmtlja, rtv pa ne mara requestov)
#for i in range(1,k):
#    page = urlji_arhiva_24ur[i-1]
#    filename = ime_datotek_htmljev_24ur[i-1]
#    directory = "arhiv_directory_24ur"
#    save_frontpage(page, directory, filename)

#for i in range(1,k):
#    page = urlji_arhiva_RTV[i-1]
#    filename = ime_datotek_htmljev_RTV[i-1]
#    directory = arhiv_directory_RTV
#    save_frontpage(page, directory, filename)  

#knjiznica requests ne zeli sodelovati z urlji RTV, zato poskusimo modul selenium:

def download_url_to_string_selenium(url):
    #browser = webdriver.Firefox()
    browser.get(url)
    content = browser.page_source
    return content

def save_frontpage_selenium(page, directory, filename):
    """Nalozi stran z url 'Page' in jo prepise v nov file. Podobno kot save frontpage, le da ta uporabi modul selenium"""
    html_strani = download_url_to_string_selenium(page)
    save_string_to_file(html_strani, directory, filename)
#nalozimo strani arhiva rtv:
def nalozi_html_od_RTV():
    """Iz arhiva nalozi htmlje v tekstovne dokumente"""
    st = 0
    directory = arhiv_directory_RTV
    for lst in urlji_arhiva_RTV.values():
        for page in lst:
            st += 1 
            filename = ime_datotek_htmljev_RTV[st-1]
            print(f"{st} od {s}")
            save_frontpage_selenium(page, directory, filename)
            time.sleep(0.5)
    '''for j in range(1,k):
        page = urlji_arhiva_RTV[j-1]
        directory = arhiv_directory_RTV
        filename = ime_datotek_htmljev_RTV[j-1]
        save_frontpage_selenium(page, directory, filename)'''
#deluje!



#zdaj iz htmlja izluscimo url in naslov vsakega clanka na doloceni strani:
#izluscili bomo tudi cas objave.
v1 = r'<p class="media-meta m-0">(?P<cas>.+?).?</p>'
v2 = r'.*?<a onclick="customNativeShare(?P<naslov>.+?),null,(?P<link>.*?);.+?</div>'
#vzorec_url_in_naslov_rtv = v1 + v2
v_naslov_datum_url = r'<div class="article-archive-item" date-is="(?P<datum>.+?)">.+?<div class="md-news">.+?<a href="(?P<url>.+?)" class=".+?" title="(?P<naslov>.+?)"'
#s = {}
#with open("RTV_stran_arhiva_1", "r", encoding='utf-8') as d:
#    niz = d.read()

#for najdba in re.finditer(v1 + v2, niz, flags=re.DOTALL):
#    cas = najdba["cas"].strip()
#    naslov = najdba["naslov"][2:].strip()
#    link = najdba["link"][1:-2].strip()
#   s[naslov] = [cas, link]
#print(s)
#deluje!
#napisimo funkcijo:
def dobi_naslov_cas_url_izarhiva_rtv(vhod):
    """Funkcija, ki iz datoteke 'vhod', ki je html arhiva rtv, izlusci naslov, cas objave in url clankov. Vrne ustrezen slovar, čigar kljuci so naslovi"""
    clanki = {}
    with open(vhod, "r", encoding='utf-8') as v:
        html = v.read()
    
    for najdba in re.finditer(v_naslov_datum_url, html, flags=re.DOTALL):
        cas = najdba["datum"]
        naslov = najdba["naslov"]
        link ="https://www.rtvslo.si" + najdba["url"]
        clanki[naslov] = [cas, link]
        
        
    return clanki

#definirajmo funkcijo, ki bo iz vec html daatotek za arhiv rtv naredila en velik seznam:
def iz_vec_html_za_arhiv_dobi_velik_slovar(sez):
    """Iz seznama datotoek, v katerih so spisani htmlji strani arhiva RTV, dobimo seznam. Kljuci so naslovi člankov, vrednosti pa seznam : [cas objace, url clanka]"""
    s = {}
    os.chdir(arhiv_directory_RTV)
    for dat in sez:
        slovar = dobi_naslov_cas_url_izarhiva_rtv(dat)
        for kljuc in slovar:
            s[kljuc] = slovar[kljuc]
        
    return s 
#print(iz_vec_html_za_arhiv_dobi_velik_slovar(ime_datotek_htmljev_RTV).keys())

#nalozimo veliko htmljev:

nalozi_html_od_RTV()

#dobimo slovar:

clanki = iz_vec_html_za_arhiv_dobi_velik_slovar(ime_datotek_htmljev_RTV)

end = time.time()
print(end-start)
#shranimo v json datoteko:
os.chdir('..')
os.chdir('..')
os.chdir("testi")
with open("JSON_RTV1.json", "w", encoding='utf-8') as d:
    json.dump(clanki, d)

print(len(clanki))
