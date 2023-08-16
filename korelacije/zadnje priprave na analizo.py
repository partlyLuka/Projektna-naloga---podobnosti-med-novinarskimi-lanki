#zadnje priprave na analizo
import os 
import json
import random
import csv
import statistics

with open("RTV_racuni.json", "r", encoding='utf-8') as dat:
    R = json.load(dat)
with open("SIOL_racuni.json", "r", encoding='utf-8') as dat:
    S = json.load(dat)
nas = random.choice(list(R.keys()))

os.chdir("..")
os.chdir("analiza_podatkov")
print(os.getcwd())
def popravi_v_datume_in_mesece(s):
    for k in s:
        niz = s[k]["cas"]
        datum, _ = niz.split("T")
        y, m, d = datum.split("-")
        s[k]["datum"] = datum
        s[k]["mesec"] =  y + m
popravi_v_datume_in_mesece(R) 
popravi_v_datume_in_mesece(S) 
novi_S = {}
for k in S:
    if len(S[k]["podobnost"]) == 3:
       novi_S[k] = S[k]
print(f"Zaradi zamika v času smo odstranili : {len(S) - len(novi_S)} člankov iz siola") 
S = novi_S

novi_R = {}
for k in R:
    if len(R[k]["podobnost"]) == 3:
       novi_R[k] = R[k]
print(f"Zaradi zamika v času smo odstranili : {len(R) - len(novi_R)} člankov iz rtv")              
R = novi_R                  
              

with open("SIOL.csv", "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "rubrika", "datum", "mesec", "avtorji", "st_besed", "cos_podobnost_1", "L_podobnost_1", "zamik_objav_1[min]", "id_podobnih_1", "cos_podobnost_2", "L_podobnost_2", "zamik_objav_2[min]", "id_podobnih_2", "cos_podobnost_3", "L_podobnost_3", "zamik_objav_3[min]", "id_podobnih_3"])
    for k in S:
        writer.writerow([S[k]["id"], S[k]["rubrika"], S[k]["datum"], S[k]["mesec"], S[k]["avtor"], S[k]["dolzina"], S[k]["podobnost"][0], S[k]["l_metric"][0], S[k]["time delta"][0], S[k]["id podobnih"][0], S[k]["podobnost"][1], S[k]["l_metric"][1], S[k]["time delta"][1], S[k]["id podobnih"][1], S[k]["podobnost"][2], S[k]["l_metric"][2], S[k]["time delta"][2], S[k]["id podobnih"][2]])


with open("RTV.csv", "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "rubrika", "datum", "mesec", "avtorji", "st_besed", "cos_podobnost_1", "L_podobnost_1", "zamik_objav_1[min]", "id_podobnih_1", "cos_podobnost_2", "L_podobnost_2", "zamik_objav_2[min]", "id_podobnih_2", "cos_podobnost_3", "L_podobnost_3", "zamik_objav_3[min]", "id_podobnih_3"])
    for k in R:
        writer.writerow([R[k]["id"], R[k]["rubrika"], R[k]["datum"], R[k]["mesec"], R[k]["avtor"], R[k]["dolzina"], R[k]["podobnost"][0], R[k]["l_metric"][0], R[k]["time delta"][0], R[k]["id podobnih"][0], R[k]["podobnost"][1], R[k]["l_metric"][1], R[k]["time delta"][1], R[k]["id podobnih"][1], R[k]["podobnost"][2], R[k]["l_metric"][2], R[k]["time delta"][2], R[k]["id podobnih"][2]])

#naredimo še slovarja, s katerima bomo lahko analizirali korelacije glede na avtorje:
def avt_slovar(s, i):
    """Dobimo slovar. Ključi so avtorji. Vrednosti so 
    st. člankov, ki jih je objavil oz. je njihov soavtor,
    povprečna cos_podobnost in mediana cos_vrednosti. i pomeni, koliko kosinusnih 
    podobnosti bomo upoštevali (i največjih)"""
    avtorji = []
    for k in s:
        for avt in s[k]["avtor"]:
            if not avt in avtorji:
                if isinstance(avt, str):
                    avtorji.append(avt)
    slovar = {}
    for avt in avtorji:
        pod = []
        cnt = 0 
        for k in s:
            if avt in s[k]["avtor"]:
                pod.extend(s[k]["podobnost"][:i])
                cnt += 1 
        if pod:
            avg = statistics.mean(pod)
            mediana = statistics.median(pod)
            c9 = 0
            c8 = 0
            c7 = 0
            c6 = 0
            c5 = 0 
            for p in pod:
                if 0.9 <= p :
                    c9 += 1
                if 0.8 <= p < 0.9 :
                    c8 += 1
                if 0.7 <= p < 0.8 :
                    c7 += 1
                if 0.6 <= p < 0.7 :
                    c6 += 1
                if 0.5 <= p < 0.6 :
                    c5 += 1
        slovar[avt] = {}
        slovar[avt]["st_clankov"] = cnt
        slovar[avt]["avg"] = avg
        slovar[avt]["mediana"] = mediana 
        slovar[avt]["st_0.9+"] = c9 
        slovar[avt]["st_0.8 - 0.9"] = c8 
        slovar[avt]["st_0.7 - 0.8"] = c7 
        slovar[avt]["st_0.6 - 0.7"] = c6 
        slovar[avt]["st_0.5 - 0.6"] = c5
    return slovar

avtorji_R = avt_slovar(R, 1)
avtorji_S = avt_slovar(S, 1)
def poberi_resne_avtorje_in_dodaj_id_R(s, n):
    #avtor mora imeti vsaj n objav. Dodamo še id. 
    slovar = {}
    for avt in s:
        if s[avt]["st_clankov"] > n -1:
            slovar[avt] = s[avt]
    i = 0
    for avt in slovar:
        i += 1 
        slovar[avt]["id"] = f"A-{i}-R"    
    return slovar
def poberi_resne_avtorje_in_dodaj_id_S(s, n):
    #avtor mora imeti vsaj n objav. Dodamo še id. 
    slovar = {}
    for avt in s:
        if s[avt]["st_clankov"] > n -1:
            slovar[avt] = s[avt]
    i = 0
    for avt in slovar:
        i += 1 
        slovar[avt]["id"] = f"A-{i}-S"
    return slovar
avtorji_R = poberi_resne_avtorje_in_dodaj_id_R(avtorji_R, 20)
avtorji_S = poberi_resne_avtorje_in_dodaj_id_S(avtorji_S, 20)
         


with open("avtorji_R.csv", "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "avtor", "st_clankov", "avg_cos_podobnost", "mediana_cos_podobnost", "st_0.9-1.0", "st_0.8-0.9", "st_0.7-0.8", "st_0.6-0.7", "st_0.5-0.6"])
    for avt in avtorji_R:
        writer.writerow([avtorji_R[avt]["id"],avt, avtorji_R[avt]["st_clankov"], avtorji_R[avt]["avg"], avtorji_R[avt]["mediana"], avtorji_R[avt]["st_0.9+"], avtorji_R[avt]["st_0.8 - 0.9"], avtorji_R[avt]["st_0.7 - 0.8"], avtorji_R[avt]["st_0.6 - 0.7"], avtorji_R[avt]["st_0.5 - 0.6"]])

with open("avtorji_S.csv", "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "avtor", "st_clankov", "avg_cos_podobnost", "mediana_cos_podobnost", "st_0.9-1.0", "st_0.8-0.9", "st_0.7-0.8", "st_0.6-0.7", "st_0.5-0.6"])
    for avt in avtorji_S:
        writer.writerow([avtorji_S[avt]["id"],avt, avtorji_S[avt]["st_clankov"], avtorji_S[avt]["avg"], avtorji_S[avt]["mediana"], avtorji_S[avt]["st_0.9+"], avtorji_S[avt]["st_0.8 - 0.9"], avtorji_S[avt]["st_0.7 - 0.8"], avtorji_S[avt]["st_0.6 - 0.7"], avtorji_S[avt]["st_0.5 - 0.6"]])

