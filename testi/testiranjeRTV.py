#testiranjeRTV
import json
import os 
import datetime
meseci = ["januar", "februar", "marec", "april", "maj", "junij", "julij", "avgust", "september", "oktober", "november", "december"]
with open("RTV.json", "r", encoding='utf-8') as dat:
    clanki = json.load(dat)
#print(len(clanki))
filenames = [clanki[k]["file"] for k in clanki]
#print(filenames)
#print(os.getcwd())
os.chdir("Html_clankov_RTV")
os.chdir("Koncni_clanki_RTV")
a = 0
for file in filenames:
    with open(file, "r", encoding='utf-8') as i:
        niz = i.read()
        if "<" in niz:
            
            a += 1 
print(f"Stevilo neuspesnih htmljev je {a}")

#zgleda da so vsi članki okej.
#napisimo funkcijo s katero bomo dostopali do vsebina:
def vsebinaR(k):
    
    datoteka = clanki[k]["file"]
    with open(datoteka, "r", encoding='utf-8') as dat:
        text = dat.read()
    return text
#print(clanki["Afriški voditelji v Kijevu: To vojno je treba rešiti in moralo bi priti do miru s pogajanji"])
#for k in clanki:
#    cas = clanki[k]["cas"]
#    n1, n2 = cas.split(" ")
#    d, m, y = n1.split(".")
#    h, min = n2.split(":")
#    cas = datetime.datetime(int(y), int(m), int(d),int(h), int(min) )
#    clanki[k]["cas"] = cas 

a = 0 
def uredi_cas():
    for k in clanki:
        #27. junij 2023 ob 16.11
        
        cas = clanki[k]["cas"]
        if len(cas.split(" ")) == 5:
            d, m, y, _, t = cas.split(" ")
            d = d.replace(".", "")
             
            if len(t.split(".")) == 2:
                h, min = t.split(".")
                m = meseci.index(m) + 1
                cas = (int(y), int(m), int(d),int(h), int(min) )
        clanki[k]["cas"] = cas   
        """n1, n2 = cas.split(" ")
        d, m, y = n1.split(".")
        h, min = n2.split(":")
        cas = (int(y), int(m), int(d),int(h), int(min) )
        clanki[k]["cas"] = cas """
uredi_cas()  
a = 0 
for k in clanki:
    t = vsebinaR(k)
    if len(t) < 20:
        a += 1 
print(f'Stevilo cudnih htmljev je {a}') 
os.chdir("..")
os.chdir("..")
os.chdir("..")
os.chdir("korelacije")
print(os.getcwd())
def zadnji_popraveK():
    s = {}
    for k in clanki:
        if len(clanki[k]["cas"]) == 5:
            s[k] = clanki[k]
    return s 
i1 = len(clanki)
clanki = zadnji_popraveK()
print(f"Zadnji zavržek je {i1 - len(clanki)} članka")
with open("RTV_konec.json", "w", encoding='utf-8') as dat:
    json.dump(clanki, dat)
print(len(clanki))