#siol_testiranje
import json
import os 
import datetime
with open("SIOL.json", "r", encoding='utf-8') as dat:
    clanki = json.load(dat)
os.chdir("Clanki_html_SIOL")
os.chdir("Koncni_clanki_siol")
#print(os.getcwd())
s = {}
for k in clanki:
    cas = clanki[k]["cas"]
    if len(cas.split(" ")) == 4:
        s[k] = clanki[k]

print(f"Zaradi časa smo odstranili {len(clanki) - len(s)} člankov.")
clanki = s 
def vsebinaSIOL(k):
    datoteka = clanki[k]["file"]
    with open(datoteka, "r", encoding='utf-8') as dat:
        text = dat.read()
    return text
for k in clanki:
    cas = clanki[k]["cas"]
    d, m,y, t = cas.split(" ")
    d = int(d.replace(".", ""))
    m = int(m.replace(".", ""))
    y = int(y)
    n1, n2 = t.split(".")
    h = int(n1)
    min = int(n2)
    clanki[k]["cas"] = (y, m, d, h, min)


os.chdir("..")
os.chdir("..")
os.chdir("..")
os.chdir("korelacije")
with open("SIOL_konec.json", "w", encoding='utf-8') as dat:
    json.dump(clanki, dat)
print(len(clanki))


    


        
