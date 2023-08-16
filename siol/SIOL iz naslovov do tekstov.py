#SIOL iz naslovov do tekstov
import json
import os 
import re 
import validators
import requests
import time
from selenium import webdriver
browser = webdriver.Firefox()
#nalozimo json:
with open("JSON_SIOL1.json", "r", encoding='utf-8') as dat:
    clanki = json.load(dat)
#shranimo htmlje clankov:
for k in clanki:
    if len(list(re.finditer(r'https://siol.net/.+?/(?P<rubrika>.+?)/', clanki[k]["link"]))) == 0:
        print(clanki[k]["link"])
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

def download_url_to_string_selenium(url):
    #browser = webdriver.Firefox()
    browser.get(url)
    content = browser.page_source
    return content
def save_frontpage_selenium(page, directory, filename):
    """Nalozi stran z url 'Page' in jo prepise v nov file. Podobno kot save frontpage, le da ta uporabi modul selenium"""
    html_strani = download_url_to_string_selenium(page)
    save_string_to_file(html_strani, directory, filename)

L = len(clanki)
def shrani_Vse_htmlje_clankov():
    i = 1
    for k in clanki:
        page = clanki[k]["link"]
        save_frontpage_selenium(page, "Clanki_html_SIOL", f"Html_clanek_{i}")
        clanki[k]["file"] = f"Html_clanek_{i}"
        clanki[k]["id"] = i 
        print(f"{i} od {L}")
        i += 1 
        #time.sleep(1.5)

#POMEMBNA FUNKCIJA:
shrani_Vse_htmlje_clankov()


os.chdir("Clanki_html_SIOL")
#with open("Html_clanek_43", "r", encoding='utf-8') as v:
#    text = v.read()
v_naslov = r'<title>(?P<naslov>.+?) - siol.net</title>'
v_avtor1 = r'Avtor.*?:(?P<blok1>.+?)</span>'
v_avtor2 = r'<a href=".+?>(?P<avtor>.+?)[\n,].+?</a>'
#for n1 in re.finditer(v_avtor1, text, flags=re.DOTALL):
#    blok = n1["blok1"]
#    for n2 in re.finditer(v_avtor2, blok,flags=re.DOTALL ):
#        print(n2["avtor"])
v_rubrika = r'https://siol.net/.+?/(?P<rubrika>.+?)/' 
v_datum_cas = r'<span class="article__publish_date--date">(?P<datum>.+?);.+?</span>.+?<span class="article__publish_date--time">(?P<cas>.+?)</span>' 
#for n in re.finditer(v_datum_cas, text, flags=re.DOTALL):
#    datum = n["datum"].strip()
#    cas = n["cas"].strip()
#    print(datum)
#    print(cas)
v_intro = r'<div class="article__intro js_articleIntro">.+?<p>(?P<intro>.+?)</p>'
v_vsebina1 = r'<div class="article__main js_article js_bannerInArticleWrap">(?P<blok>.+)'
v_vsebina2 = r'<p>(.+?)</p>|<h\d>(.+?)</h\d>|<li>(.+?)</li>|<br/>\n(.+?)<br/>'
#for najdba in re.finditer(v_vsebina1, text, flags=re.DOTALL):
#    blok = najdba["blok"]
#    for n in re.finditer(v_vsebina2, blok, flags=re.DOTALL):
#        vsebina = n["vsebina"].replace("<strong>", "").replace("</strong>", "").strip()
#        print(vsebina)
#        print("\n")
def iz_html_v_txt(k):
    vhod = clanki[k]["file"]
    print(vhod)
    pisi = ""
    with open(vhod, "r", encoding='utf-8') as v:
        text = v.read() 
    for n in re.finditer(v_naslov, text, flags=re.DOTALL):
        naslov = n["naslov"] 
        pisi += naslov + "\n\n"
    avtor = []
    for n1 in re.finditer(v_avtor1, text, flags=re.DOTALL):
        blok = n1["blok1"]
        for n2 in re.finditer(v_avtor2, blok,flags=re.DOTALL ):
            avtor.append(n2["avtor"].strip())
    cas = ""
    for n in re.finditer(v_datum_cas, text, flags=re.DOTALL):
        cas += n["datum"].strip() + " " + n["cas"].strip()
    for n in re.finditer(v_intro, text, flags=re.DOTALL):
        intro = n["intro"]
        pisi += intro + "\n\n"
    for najdba in re.finditer(v_vsebina1, text, flags=re.DOTALL):
        print(len(text))
        block = najdba["blok"]
        print(len(block))
        for n in re.finditer(v_vsebina2, block, flags=re.DOTALL):
            vsebina = n.group().replace("<strong>", "").replace("</strong>", "").strip()
            naivni_vzorec = r'<(.+?)>'
            vsebina = re.sub(naivni_vzorec, "", vsebina)
            vsebina = vsebina.replace("TSmedia, medijske vsebine in storitve, d.o.o.,", "")
            vsebina = vsebina.replace("Cigaletova 15, 1000 Ljubljana,", "")
            vsebina = vsebina.replace("T: +386 1 473 00 10", "")
            vsebina = vsebina.replace("Oglejte si še:", "")
            if (not "=" in vsebina) and (not "<" in vsebina):
                pisi += vsebina + "\n\n"
    pisi = re.sub(r'<.+?>', "",pisi)
    avtorji = ", ".join(avtor)
    clanki[k]["cas"] = cas.strip()
    clanki[k]["avtor"] = avtorji
    filename = "SIOL_" + vhod.replace("Html", "Koncni")
    save_string_to_file(pisi, "Koncni_clanki_siol", filename)

#for k in clanki:
#    iz_html_v_txt(k)
#    print(clanki[k]["id"])
#vse zgleda okej. dobimo se rubriko:
def dobi_rubrika():
    for k in clanki:
        url = clanki[k]["link"]
        n = re.search(v_rubrika, url)
        if not n:
            u = re.search(r'https://siol.net/(.+?)/', url)
            if u:
                rubrika = u.group()
            continue
        rubrika = n["rubrika"]
        if not rubrika == "novice":
            clanki[k]["rubrika"] = rubrika
        else:
            n = re.search(r'https://siol.net/(?P<rubrika>.+?)/', url)
            if n:
                clanki[k]["rubrika"] = n["rubrika"]
        if '/sportal/' in url:
            clanki[k]["rubrika"] = 'sportal'
        if '/trendi/' in url:
            clanki[k]["rubrika"] = 'trendi'
        if '/dom/' in url:
            clanki[k]["rubrika"] = 'dom'
        if '/planet-tv/' in url:
            clanki[k]["rubrika"] = 'planet-tv'
        if '/posel-danes/' in url:
            clanki[k]["rubrika"] = 'posel-danes'
        if '/avtomoto/' in url:
            clanki[k]["rubrika"] = 'avtomoto'
        if '/trajnost/' in url:
            clanki[k]["rubrika"] = 'trajnost'
        if '/digisvet/' in url:
            clanki[k]["rubrika"] = 'digisvet'
        
dobi_rubrika()

for k in clanki:
    iz_html_v_txt(k)
    filename = "SIOL_" + clanki[k]["file"].replace("Html", "Koncni")
    clanki[k]["file"] = filename

os.chdir("..")
with open("SIOL.json", "w", encoding='utf-8') as d:
    json.dump(clanki, d)
