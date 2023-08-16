#izracuni
import datetime
import json 
import os 
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import enchant
import time 

start = time.time()

with open("RTV_konec.json", "r", encoding='utf-8') as dat:
    R = json.load(dat)
with open("SIOL_konec.json", "r", encoding='utf-8') as dat:
    S = json.load(dat)

def uredi_cas(s):
    for k in s:
        cas = s[k]["cas"]
        if len(cas) == 5:
            y, m, d, h, min = cas 
            s[k]["cas"] = datetime.datetime(y, m, d, h, min)
uredi_cas(R)
uredi_cas(S)
#print(S)
def vsebinaSIOL(k):
    os.chdir("..")
    os.chdir("siol")
    os.chdir("Clanki_html_SIOL")
    os.chdir("Koncni_clanki_siol")
    datoteka = S[k]["file"]
    with open(datoteka, "r", encoding='utf-8') as dat:
        text = dat.read()
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    os.chdir("korelacije")
    return text
def vsebinaRTV(k):
    os.chdir("..")
    os.chdir("testi")
    os.chdir("Html_clankov_RTV")
    os.chdir("Koncni_clanki_RTV")
    datoteka = R[k]["file"]
    with open(datoteka, "r", encoding='utf-8') as dat:
        text = dat.read()
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    os.chdir("korelacije")
    return text

def korelacija(text1, text2):
    """Izračuna cosine similarity na 6 decimalk natančno."""
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors)
    return round(similarity[0][1], 6)
"""
k = random.choice(list(R.keys()))
n = 0 
kor = 0
for nas in S:
    d1 = R[k]["cas"]
    d2 = S[nas]["cas"]  
    delta = abs(d1 - d2)        
    sim = korelacija(vsebinaRTV(k), vsebinaSIOL(nas))
    if sim > kor and -3 < delta.days < 3:
        kor = sim
        n = nas
print(kor)
print(R[k]["cas"], len(vsebinaRTV(k)))
print(S[n]["cas"], len(vsebinaSIOL(n)))
print(R[k]["cas"] - S[n]["cas"])
print(k)
print(n)
print(R[k]["url"])
print(S[n]["link"])"""
"""
m = 0
vr = 0
for n in S:
    m += 1 
    vr += len(vsebinaSIOL(n))
print(vr/m)"""
"""
for u in S:
    if u == "Vlada bo zahtevala vračilo neupravičeno prejete pomoči #video":
        print(len(vsebinaSIOL(u)))"""
#dajmo popraviti R in S, če je potrebno:
def popravi(s):
    for k in s:
        if not "rubrika" in s[k]:
            s[k]["rubrika"] = None
popravi(R)
popravi(S)
 

def leven(s1, s2):
    """Izračuna levenshteinovo razdaljo med s1 in s2(niza)"""
    return enchant.utils.levenshtein(s1, s2) 

#čas je, da napišemo kardinalno funkcijo:
def PrintPodobniRTV(clanek, t1, t2, i0):
    """Vzame članek 'clanek' iz rtv, poišče i0 člankov iz siola, ki so bili napisani
    t1 dni pred do t2 dni po objavi članka 'clanek' in ki so najbolj podobni članku 'clanek'
    glede na cosine similarity. Povrh še zračuna levenshtein razdaljo med naslovi. Uporabne 
    podatke naposled sprinta."""
    kandidati = []
    date1 = R[clanek]["cas"]
    vsebina = vsebinaRTV(clanek)
    for k in S:
        date2 = S[k]["cas"]
        delta = -(date1 - date2).days
        if -t1 < delta < t2:
            kor = korelacija(vsebina, vsebinaSIOL(k))
            kandidati.append([kor, k])
    kandidati.sort(reverse=True)
    i = min(i0 + 1, len(kandidati))
    ozji_izbor = kandidati[:i - 1]
    novi_ozji_izbor = []
    for lst in ozji_izbor:
        kor, naslov = lst
        l_metric = leven(clanek, naslov)
        podatek = [kor, l_metric, naslov]
        novi_ozji_izbor.append(podatek)
    novi_ozji_izbor.sort(reverse=True)
    for kor, l, nas in novi_ozji_izbor:
        print(kor, l)
        print(f"Siol:{nas}")
        print(f"RTV:{clanek}")
        print(f"Link: {S[nas]['link']}")
        print(f"Link: {R[clanek]['url']}")
        print(f'Objava na rtv: {R[clanek]["cas"]}')
        print(f'Objava na siol: {S[nas]["cas"]}')
        print("XXX")       
def PodobniRTV(clanek, t1, t2, i0):
    """Vzame članek 'clanek' iz rtv, poišče i0 člankov iz siola, ki so bili napisani
    t1 dni pred do t2 dni po objavi članka 'clanek' in ki so najbolj podobni članku 'clanek'
    glede na cosine similarity. Povrh še zračuna levenshtein razdaljo med naslovi. Naposled vrne seznam seznamov oblike:
    [korelacija, levenshteinova razdalja, časovna razlika objav v sekundah, naslov, id], za najpodobnejše članke iz siola"""
    kandidati = []
    date1 = R[clanek]["cas"]
    vsebina = vsebinaRTV(clanek)
    for k in S:
        date2 = S[k]["cas"]
        delta = -(date1 - date2)
        if -t1 < delta.days < t2:
            kor = korelacija(vsebina, vsebinaSIOL(k))
            kandidati.append([kor, k, -delta.total_seconds(), S[k]["id"]])
    kandidati.sort(reverse=True)
    i = min(i0 + 1, len(kandidati))
    ozji_izbor = kandidati[:i - 1]
    novi_ozji_izbor = []
    for lst in ozji_izbor:
        kor, naslov, delta, id = lst
        l_metric = leven(clanek, naslov)
        podatek = [kor, l_metric, delta, naslov, id]
        novi_ozji_izbor.append(podatek)
    novi_ozji_izbor.sort(reverse=True) 
    return novi_ozji_izbor      
def PodobniSIOL(clanek, t1, t2, i0):
    """Vzame članek 'clanek' iz siola, poišče i0 člankov iz rtv, ki so bili napisani
    t1 dni pred do t2 dni po objavi članka 'clanek' in ki so najbolj podobni članku 'clanek'
    glede na cosine similarity. Povrh še zračuna levenshtein razdaljo med naslovi. Naposled vrne seznam seznamov oblike:
    [korelacija, levenshteinova razdalja, časovna razlika objav v sekundah, naslov, id], za najpodobnejše članke iz rtv"""
    kandidati = []
    date1 = S[clanek]["cas"]
    vsebina = vsebinaSIOL(clanek)
    for k in R:
        date2 = R[k]["cas"]
        delta = -(date1 - date2)
        if -t1 < delta.days < t2:
            kor = korelacija(vsebina, vsebinaRTV(k))
            kandidati.append([kor, k, -delta.total_seconds(),  R[k]["id"]])
    kandidati.sort(reverse=True)
    i = min(i0 + 1, len(kandidati))
    ozji_izbor = kandidati[:i - 1]
    novi_ozji_izbor = []
    for lst in ozji_izbor:
        kor, naslov, delta, id = lst
        l_metric = leven(clanek, naslov)
        podatek = [kor, l_metric, delta, naslov, id]
        novi_ozji_izbor.append(podatek)
    novi_ozji_izbor.sort(reverse=True) 
    return novi_ozji_izbor
def PrintPodobniSIOL(clanek, t1, t2, i0):
    """Vzame članek 'clanek' iz siola, poišče i0 člankov iz rtv, ki so bili napisani
    t1 dni pred do t2 dni po objavi članka 'clanek' in ki so najbolj podobni članku 'clanek'
    glede na cosine similarity. Povrh še zračuna levenshtein razdaljo med naslovi. Uporabne 
    podatke naposled sprinta."""
    kandidati = []
    date1 = S[clanek]["cas"]
    vsebina = vsebinaSIOL(clanek)
    for k in R:
        date2 = R[k]["cas"]
        delta = -(date1 - date2).days
        if -t1 < delta < t2:
            kor = korelacija(vsebina, vsebinaRTV(k))
            kandidati.append([kor, k])
    kandidati.sort(reverse=True)
    i = min(i0 + 1, len(kandidati))
    ozji_izbor = kandidati[:i - 1]
    novi_ozji_izbor = []
    for lst in ozji_izbor:
        kor, naslov = lst
        l_metric = leven(clanek, naslov)
        podatek = [kor, l_metric, naslov]
        novi_ozji_izbor.append(podatek)
    novi_ozji_izbor.sort(reverse=True)
    for kor, l, nas in novi_ozji_izbor:
        print(kor, l)
        print(f"RTV:{nas}")
        print(f"Siol:{clanek}")
        print(f"Link:{R[nas]['url']}")
        print(f"Link: {S[clanek]['link']}")
        print(f'Objava na siol:{S[clanek]["cas"]}')
        print(f'Objava na rtv: {R[nas]["cas"]}')
        print("XXX")
#lst = [[1,3], [33,33], [12,14], [-4,5]]
#lst.sort(reverse=True)
#print(lst)
naslov = random.choice(list(R.keys()))
#print(PodobniRTV(naslov, 10, 10, 1))
#print({R[k]["rubrika"] for k in R})

#popravimo id-je. Zaznamovali jih bomo glede na to, ali je članek iz rtv ali iz siola.
def id_ureditev_R():
    for k in R:
        id = R[k]["id"]
        novi_id = str(id) + "-R"
        R[k]["id"] = novi_id

def id_ureditev_S():
    for k in S:
        id = S[k]["id"]
        novi_id = str(id) + "-S"
        S[k]["id"] = novi_id
        
id_ureditev_R()
id_ureditev_S()
#zdaj bomo za res kaj poračunali:
#odločili smo se, da bo časovna toleranca 5 dni, vzeli bomo 4 najpodobnejše
def izracunR(k, t1, n):
    """za članek 'k' iz rtv pobere n najpodobnejših člankov, ki so bili objavljeni
    t1 dni prej na siolu in shrani pomembne informacije:
    st besed prvotnega članka, kosinusno podobnost, L podobnost,
    id podobnih člankov ter časovne razlike med objavami prvotnega članka
    in vsakega od podobnih(v minutah)."""
    content = vsebinaRTV(k)
    dolzina = len(content.split())
    podatki = PodobniRTV(k, t1, 0, n)
    R[k]["podobnost"] = []
    R[k]["l_metric"] = []
    R[k]["id podobnih"] = [] 
    R[k]["time delta"] = [] 
    for podatek in podatki:
        kor, l_metric, delta, naslov, id = podatek
        R[k]["podobnost"].append(kor)
        R[k]["l_metric"].append(l_metric)
        R[k]["id podobnih"].append(id)
        R[k]["time delta"].append(delta/60) 
    R[k]["dolzina"] = dolzina
           
def izracunS(k, t1, n):
    """za članek 'k' iz siola pobere n najpodobnejših člankov, ki so bili objavljeni
    t1 dni prej na rtv in shrani pomembne info:
    st besed prvotnega članka, kosinusno podobnost, L podobnost,
    id podobnih člankov ter časovno razliko med objavami prvetnoga članka ter
    vsakega od podobnih člankov posebej(v minutah)."""
    content = vsebinaSIOL(k)
    dolzina = len(content.split())
    podatki = PodobniSIOL(k, t1, 0, n)
    S[k]["podobnost"] = []
    S[k]["l_metric"] = []
    S[k]["id podobnih"] = [] 
    S[k]["time delta"] = []
    for podatek in podatki:
        kor, l_metric, delta, naslov, id = podatek
        S[k]["podobnost"].append(kor)
        S[k]["l_metric"].append(l_metric)
        S[k]["id podobnih"].append(id)
        S[k]["time delta"].append(delta/60)
    S[k]["dolzina"] = dolzina

def celoten_izracun_RTV(t1, n):
    #t1 in n pomenita isto kot zgoraj
    for k in R:
        izracunR(k, t1, n)
        print(R[k]["id"])

def celoten_izracun_SIOL(t1, n):
    #t1 in n pomenita isto kot zgoraj
    for k in S:
        izracunS(k, t1, n)
        print(S[k]["id"])

#NAJPOMEMBNEJŠI FUNKCIJI:

celoten_izracun_RTV(5, 3)
celoten_izracun_SIOL(5, 3)

###########################
"""ss = random.choice(list(S.keys()))
print(S[ss]["link"])
print(PodobniSIOL(ss, 3, 0, 1))
id = PodobniSIOL(ss, 3, 0, 1)[0][-1]
print(id)
for k in R:
    if R[k]["id"] == id:
        print(R[k]["url"])  
"""
x = 0
#for k in R:
#    if R[k]["podobnost"]:
#        p = R[k]["podobnost"][0]
#        if p > 0.8:
#            x += 1 

end = time.time()
#še zadnja stvar je, da uredimo avtorje in datetime.datetime objekte pretvorimo v nize, da jih bomo lahko shranili v JSON
#l = random.choice(list(R.keys()))
#PrintPodobniRTV(l, -1, 5, 3)
def popravi_avtorje_in_cas_R():
    for k in R:
        if isinstance(R[k]["cas"], datetime.datetime):
            R[k]["cas"] = R[k]["cas"].isoformat()
        if R[k]["avtor"]:
            avt = R[k]["avtor"].replace(", Program Ars", "")
            avt = avt.replace("(Oddaja Avtomobilnost)", "")
            avt = avt.replace("(Avtomobilnost)", "")
            avt = avt.strip()
            avt = avt.split(", ")
            R[k]["avtor"] = avt
popravi_avtorje_in_cas_R()

def popravi_avtorje_S():
    for k in S:
        if isinstance(S[k]["cas"], datetime.datetime):
            S[k]["cas"] = S[k]["cas"].isoformat()
        if S[k]["avtor"]:
            avt = S[k]["avtor"].replace("VIDEO: ", "")
            avt = avt.strip()
            avt = avt.split(", ")
            S[k]["avtor"] = avt
popravi_avtorje_S()

with open("RTV_racuni.json", "w", encoding='utf-8') as dat:
    json.dump(R, dat)

with open("SIOL_racuni.json", "w", encoding='utf-8') as dat:
    json.dump(S, dat)

