#RTV-iz naslovov do besedilo
import json
import os 
import re 
from selenium import webdriver
browser = webdriver.Firefox()
import validators
import requests
import time

start = time.time()





#nalozimo json:
with open("JSON_RTV1.json", "r", encoding='utf-8') as dat:
    clanki = json.load(dat)
#for k,v in clanki.items():
#    print(k)
#    print(v)
#problem so clanki, ki so v celoti en citat. Poskusimo to popraviti!
"""s = {}
a = 0
for k, v in clanki.items():
    if '"' in k:
        s[k] = v
for k, v in s.items():
    print(k)
    print(v[0])
    print(v[1])
    print(" ")
print('https://www.rtvslo.si/svet/preberite-tudi/papez-tudi-drugo-noc-po-operaciji-prezivel-mirno/671243')
#poskusajmo nazaj sestaviti urlje:
nov = {}
for k, v in s.items():
    url = v[1].replace(" ", "").replace('=""', '/').replace(':/', '://')
    v[1] = url
    #print(url)
    #urlji so popravljeni! Popravimo še naslove:
    naslov = k.replace("=", "").replace(" ", "").replace('""', ' ').replace('"', '').capitalize()
    print(naslov)
    nov[naslov] = v
    #uspelo je! 
"""
def popravi_naslove_s_citiati_RTV(s):
    """Funkcija popravi nepravilnosti, ki se pojavijo pri clankih, katerih naslovi so v celoti en citat"""
    novi = {}
    for k, v in s.items():
        if '"' in k:
            #ti imajo napako
            naslov = k.replace("=", "").replace(" ", "").replace('""', ' ').replace('"', '').capitalize()
            url = v[1].replace(" ", "").replace('=""', '/').replace(':/', '://')
            v[1] = url
            novi[naslov] = v
        else:
            novi[k] = v 
    return novi
clanki = popravi_naslove_s_citiati_RTV(clanki)
urlji = [clanki[k][1] for k in clanki]
def popravi_vrzi_ven_skit_rubriko(s):
    novi = {}
    for k, v in s.items():
        url = v[1]
        if not 'https://www.rtvslo.si/skit/' in url:
            novi[k] = v
    return novi 
clanki = popravi_vrzi_ven_skit_rubriko(clanki)
#z modulom validators preverimo, da so vsi link legitimni:
#a = 0 
#for k, v in clanki.items():
#    url = v[1]
#    if validators.url(url):
#        a += 1
#print(a)
#print(len(clanki))
#stevilke se ujemajo!!!

#for k, v in clanki.items():
#    print(k)
def preveri_ali_so_url_ok(s):
    for k, v in s.items():
        url = v[1]
        if not validators.url(url):
            print(clanki[k])
            return False
    return True
#if not preveri_ali_so_url_ok(clanki):
#    raise ValueError(f"Vsi urlji niso ok")
def download_url_to_string_selenium(url):
    #browser = webdriver.Firefox()
    browser.get(url)
    content = browser.page_source
    return content

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

def save_frontpage_selenium(page, directory, filename):
    """Nalozi stran z url 'Page' in jo prepise v nov file. Podobno kot save frontpage, le da ta uporabi modul selenium"""
    html_strani = download_url_to_string_selenium(page)
    save_string_to_file(html_strani, directory, filename)


#vsakemu clanku bomo pripisali stevilko:
e = 0
v_rubrika = r'si/(?P<r>.+?)/'
for k in clanki:
    e += 1
    url = clanki[k][1]
    najdba = re.search(v_rubrika, url)
    clanki[k].append(najdba["r"])
    clanki[k] += [e]
    



#print(clanki) 
#naredimo mapo, kamor bomo shranili tekstovne dokumente z vsebino vsakega clanka. V slovarju bomom podali pot so ustreznega dokumenta.
#print(os.getcwd())

#print(os.getcwd())
vsi = len(clanki)
def shrani_html_clankov(s):
    for k, v in s.items():
        url = v[1]
        st = v[3]
        print(f"{st} od {vsi}")
        naslov = f'Clanek_RTV_html_{st}'
        save_frontpage_selenium(url, 'Html_clankov_RTV', f"{naslov}")

shrani_html_clankov(clanki)
#print(os.getcwd())
#malo uredimo glavni slovar:
def uredi(s):
    novi = {}
    cnt = 0 
    for k, v in s.items():
        naslov = k
        date_time = v[0]
        url = v[1]
        rubrika = v[2]
        id = 0 
        if not "skit" == rubrika:
            cnt += 1
            id = cnt
            novi[naslov] = {}
            novi[naslov]["cas"] = date_time
            novi[naslov]["rubrika"] = rubrika
            novi[naslov]["id"] = id
            novi[naslov]["url"] = url
    return novi 
clanki = uredi(clanki)

#zdaj bomo izluscili vsebino:
#dobimo avorja:

v_avtor = r'name="author" content="(?P<avtor>.+?)">'
os.chdir("..")
#with open("Clanek 1", "r", encoding='utf-8') as f:
#    text = f.read()
#for najdba in re.finditer(v_avtor, text, flags=re.DOTALL):
#    print(najdba["avtor"])
#deluje.
#izlzscimo naslov
v_naslov = r'<meta name="title" content="(?P<nas>.+?)">'
v_cas = r'<div class="publish-meta">(?P<cas>.+?)<'

#for n in re.finditer(v_naslov, text, flags=re.DOTALL):
#    naslov = n["nas"]
v_subtitle = r'<div class="subtitle">(?P<sub>.+?)</div>'
##for n in re.finditer(v_subtitle, text, flags=re.DOTALL):
#    print(n["sub"])
v_povzetek = r'<p class="lead">(?P<pov>.+?)</p>'
#for n in re.finditer(v_povzetek, text, flags=re.DOTALL):
#    print(n["pov"])
v_sirokovsebino = r'<article class="article">(?P<blok>.+?)</article>'
#for n in re.finditer(v_sirokovsebino, text, flags=re.DOTALL):
#    blok = n["blok"]
    
v_ozja_vsebina = r'<p>(.+?)</p>|<h\d>(.+?)</h\d>'

#pisi = ""
#for n in re.finditer(v_ozja_vsebina, blok, flags=re.DOTALL):
#    vsebina = n.group()
#    naivni_vzorec = r'<(.+?)>'
#    vsebina = re.sub(naivni_vzorec, "", vsebina)
#    pisi += vsebina
#    print(vsebina)
#napisimo funkcijo, ki bo iz html datoteke izluscila vsebina in jo prepisala v tekstovni dokument
vsi = len(clanki)
def iz_html_v_text(vhod, directory, filename):
    pisi = ""
    with open(vhod, "r", encoding='utf-8' ) as v:
        text = v.read()
        #bilo bi dobro dobiti naslov clanki, v katerem smo:
        niz = vhod
        lst = niz.split("_")
        ID = int(lst[-1])
        for k in clanki:
            if clanki[k]["id"] == ID:
                keyy = k 
        print(f"{ID} od {vsi}")        
        #avtor:
        for najdba in re.finditer(v_avtor, text, flags=re.DOTALL):
            avtor = najdba["avtor"]
            if najdba["avtor"]:
                clanki[keyy]["avtor"] = avtor
            else:
                clanki[keyy]["avtor"] = None
        for najdba in re.finditer(v_cas, text, flags=re.DOTALL):
            cas = najdba["cas"]
            if najdba["cas"]:
                clanki[keyy]["cas"] = cas.strip() 
            else:
                clanki[keyy]["cas"] = None   
        v = vhod.replace("html", "koncni")
        clanki[keyy]["file"] = v
        #naslov:
        for n in re.finditer(v_naslov, text, flags=re.DOTALL):
            naslov = n["nas"]
        if not list(re.finditer(v_naslov, text, flags=re.DOTALL)):
            save_string_to_file("Čuden html", directory, filename)
            return None 
        pisi += naslov + "\n\n"
        for n in re.finditer(v_subtitle, text, flags=re.DOTALL):
            subtitle = n["sub"]
            if not "<" in subtitle:
                pisi += subtitle + "\n\n"
        for n in re.finditer(v_povzetek, text, flags=re.DOTALL):
            povzetek = n["pov"]
            if not "<" in povzetek:    
                pisi += povzetek + "\n\n"
        for n in re.finditer(v_sirokovsebino, text, flags=re.DOTALL):
            blook = n["blok"]
            if n["blok"]:
                for n in re.finditer(v_ozja_vsebina, blook, flags=re.DOTALL):
                    vsebina = n.group()
                    naivni_vzorec = r'<(.+?)>'
                    vsebina = re.sub(naivni_vzorec, "", vsebina)
                    if not "<" in vsebina:
                        pisi += vsebina + "\n\n"
    
    save_string_to_file(pisi, directory, filename)
#iz_html_v_text("Clanek 1", "Koncni clanki RTV", "Clanek_1")
#iz vseh htmljev naredimo tekstovne dokumente:
os.chdir("testi")
os.chdir("Html_clankov_RTV")
#print(os.listdir())
def iz_vec_html_do_tekstov():
    #iz direktorija pobere htmlje in jih zapise v tekste
    for i in range(1,len(clanki)+1) :
        file = f"Clanek_RTV_html_{i}"
        print(file)
        filename = file.replace("html", "koncni")
        iz_html_v_text(file, "Koncni_clanki_RTV", filename)
iz_vec_html_do_tekstov()
            
#iz_html_v_text("Clanek_RTV_html_123", "Koncni", "koncani_100")     
#os.chdir("..")
#malo uredimo glavni slovar:



            
#iz_html_v_text("Clanek_RTV_html_123", "Koncni", "koncani_100") 
print(f"Zaradi rubrike skit smo izbrisali {len(urlji)- len(clanki)} clanek")
#print(clanki)
#vidimo, da so nekateri avtorji zelo čudni. To je zato, ker so to poročilo od STA. Popravimo!
for k in clanki:
    if "avtor" in clanki[k]:
        avt = clanki[k]["avtor"]
        if "=" in avt or "<" in avt:
            clanki[k]["avtor"] = "STA"
    else:
        clanki[k]["avtor"] = None
print(clanki)
#imamo koncni slovar
#Kaj vse naredi ta skripta?:
#dobi slovar z urlji clankoc, zapise njihove vsebine in naredi slovar s podatki clankov. V slocarju so imena tekstovnega dokumenta, v katerem je vsebina članka
os.chdir("..")
with open("RTV.json", "w", encoding='utf-8') as d:
    json.dump(clanki, d)
end = time.time()
print(end-start) 
print(f"Zaradi rubrike skit smo izbrisali {len(urlji)- len(clanki)} clanek")
print(len(clanki))              
        

