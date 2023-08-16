#testi za requests
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import os
import time
googleURL = "https://www.rtvslo.si/novice?p=4"

#browser = webdriver.Firefox()
#browser.get(googleURL)
#content = browser.page_source
#print(len(content))
#soup = BeautifulSoup(content)
niz = '''Šlo je za sterilizacijo v skladu s spornim zakonom, ki je bil v veljavi 48 let. V skladu z njim so pri prebivalcih, ki so bili ožigosani kot manjvredni, največkrat je šlo za osebe z motnjami v razvoju, z duševnimi boleznimi ali dednimi boleznimi, izvedli sterilizacijo, da bi "preprečili rojstvo potomcev z nizko kakovostjo življenja", kot je bilo zapisano v zakonu.

Med steriliziranimi sta bila tudi komaj devetletna deklica in deček, razkriva poročilo, ki je sprožilo oster odziv številnih organizacij.

Še nadaljnjih 8000 ljudi je privolilo v sterilizacijo, a so bili v soglasje najverjetneje prisiljeni, poroča Guardian. Kot razkriva poročilo, je bilo še skoraj 60.000 žensk prisiljenih splaviti zaradi dednih bolezni.

Žrtve in njihovi sorodniki si že leta prizadevajo za razgaljenje diskriminatornega odnosa japonskih oblasti do ljudi s posebnimi potrebami in kroničnimi boleznimi v obdobju po koncu druge svetovne vojne.
Izplačanih le 1049 zahtevkov

Leta 2019 je japonski parlament sprejel zakon, po katerem so vsaki žrtvi ponudili približno 22.800 evrov odškodnine. Predstavniki organizacij za človekove pravice so znesek označili za premajhen. Kot navajajo japonski mediji, se rok za izplačilo odškodnine izteče aprila 2024, doslej pa so jih izplačali le 1049.

Doslej so štiri sodišča odločila, da je treba izplačati odškodnine, druga sodišča pa so zahtevke zavrnila, češ da je že minilo 20-letno obdobje, ko je bilo to mogoče. Odvetniki žrtev so vztrajali, da so bile njihove žrtve o operacijah, ki so jih izvedli na njih, obveščeni prepozno, da bi lahko ujeli zakonske roke.

Podobni zakonodaji sta veljali tudi v Nemčiji in na Švedskem, kjer so se žrtvam opravičili in že izplačali odškodnine.
Prisilna sterilizacija jo je stala zakona in družine

Japonsko sodišče je pretekli mesec zavrnilo zahtevo za izplačilo odškodnine, ki ga je vložila danes 77-lena Junko Iizuka. Pri 16 letih so jo odpeljali na kliniko na severovzhodu države in jo prisilili v neznano operacijo, pozneje se je izkazalo, da so jo sterilizirali. "Ta operacija me je oropala mojih sanj o srečnem zakonu in otrocih." Ko je pozneje odkrila, kaj se ji je zgodilo, je to povedala možu, ta pa jo je zapustil in zahteval ločitev. "Duševno sem zbolela in nisem mogla delati. Diagnosticirali so mi posttravmatski stres. Ta operacija je moje življenje postavila na glavo."

Po objavi poročila se je v imenu vlade državni sekretar v premierjevem uradu Hirokazu Macuno opravičil žrtvam za "nepredstavljivo bolečino," ki so jo utrpele.

"Poročilo ni osvetlilo, zakaj je bil tak zakon sploh sprejet, zakaj je trajalo 48 let, da so ga ukinili, in zakaj žrtve niso nikoli prejele odškodnine," je dejal zastopnik žrtev Koji Nisato.'''


niz = niz.replace("\n", "").replace("\t", "")
print(len(niz))

#with open("test2", "w", encoding='utf-8') as i:
#    print(niz, file=i)
k = '''Japonsko pretresa poročilo o prisilni sterilizaciji okoli 16.500 ljudi z različnimi težavami

Le redke žrtve so vložile zahtevek za izplačilo odškodnine

Japonski parlament je ta teden sprejel 1400 strani dolgo poročilo, ki razkriva, da so med letoma 1948 in 1996 brez soglasja sterilizirali okoli 16.500 ljudi, velika večina so bila dekleta, najmlajši med žrtvami sta bili stari le devet let. 

Šlo je za sterilizacijo v skladu s spornim zakonom, ki je bil v veljavi 48 let. V skladu z njim so pri prebivalcih, ki so bili ožigosani kot manjvredni, največkrat je šlo za osebe z motnjami v razvoju, z duševnimi boleznimi ali dednimi boleznimi, izvedli sterilizacijo, da bi "preprečili rojstvo potomcev z nizko kakovostjo življenja", kot je bilo zapisano v zakonu.

Med steriliziranimi sta bila tudi komaj devetletna deklica in deček, razkriva poročilo, ki je sprožilo oster odziv številnih organizacij.

Še nadaljnjih 8000 ljudi je privolilo v sterilizacijo, a so bili v soglasje najverjetneje prisiljeni, poroča Guardian. Kot razkriva poročilo, je bilo še skoraj 60.000 žensk prisiljenih splaviti zaradi dednih bolezni. 

Žrtve in njihovi sorodniki si že leta prizadevajo za razgaljenje diskriminatornega odnosa japonskih oblasti do ljudi s posebnimi potrebami in kroničnimi boleznimi v obdobju po koncu druge svetovne vojne.

Izplačanih le 1049 zahtevkov

Leta 2019 je japonski parlament sprejel zakon, po katerem so vsaki žrtvi ponudili približno 22.800 evrov odškodnine. Predstavniki organizacij za človekove pravice so znesek označili za premajhen. Kot navajajo japonski mediji, se rok za izplačilo odškodnine izteče aprila 2024, doslej pa so jih izplačali le 1049. 

Doslej so štiri sodišča odločila, da je treba izplačati odškodnine, druga sodišča pa so zahtevke zavrnila, češ da je že minilo 20-letno obdobje, ko je bilo to mogoče.  Odvetniki žrtev so vztrajali, da so bile njihove žrtve o operacijah, ki so jih izvedli na njih, obveščeni prepozno, da bi lahko ujeli zakonske roke. 

Podobni zakonodaji sta veljali tudi v Nemčiji in na Švedskem, kjer so se žrtvam opravičili in že izplačali odškodnine. 

Prisilna sterilizacija jo je stala zakona in družine

Japonsko sodišče je pretekli mesec zavrnilo zahtevo za izplačilo odškodnine, ki ga je vložila danes 77-lena Junko Iizuka. Pri 16 letih so jo odpeljali na kliniko na severovzhodu države in jo prisilili v neznano operacijo, pozneje se je izkazalo, da so jo sterilizirali. "Ta operacija me je oropala mojih sanj o srečnem zakonu in otrocih." Ko je pozneje odkrila, kaj se ji je zgodilo, je to povedala možu, ta pa jo je zapustil in zahteval ločitev. "Duševno sem zbolela in nisem mogla delati. Diagnosticirali so mi posttravmatski stres. Ta operacija je moje življenje postavila na glavo."

Po objavi poročila se je v imenu vlade državni sekretar v premierjevem uradu Hirokazu Macuno opravičil žrtvam za "nepredstavljivo bolečino," ki so jo utrpele. 

"Poročilo ni osvetlilo, zakaj je bil tak zakon sploh sprejet, zakaj je trajalo 48 let, da so ga ukinili, in zakaj žrtve niso nikoli prejele odškodnine," je dejal zastopnik žrtev Koji Nisato.
'''
print(len(k))

l = '''Japonsko pretresa poročilo o prisilni sterilizaciji okoli 16.500 ljudi z različnimi težavami
Le redke žrtve so vložile zahtevek za izplačilo odškodnine

Japonski parlament je ta teden sprejel 1400 strani dolgo poročilo, ki razkriva, da so med letoma 1948 in 1996 brez soglasja sterilizirali okoli 16.500 ljudi, velika večina so bila dekleta, najmlajši med žrtvami sta bili stari le devet let.
K. T.
22. junij 2023 ob 16.53
MMC RTV SLO
Foto: Reuters
Foto: Reuters

Šlo je za sterilizacijo v skladu s spornim zakonom, ki je bil v veljavi 48 let. V skladu z njim so pri prebivalcih, ki so bili ožigosani kot manjvredni, največkrat je šlo za osebe z motnjami v razvoju, z duševnimi boleznimi ali dednimi boleznimi, izvedli sterilizacijo, da bi "preprečili rojstvo potomcev z nizko kakovostjo življenja", kot je bilo zapisano v zakonu.

Med steriliziranimi sta bila tudi komaj devetletna deklica in deček, razkriva poročilo, ki je sprožilo oster odziv številnih organizacij.

Še nadaljnjih 8000 ljudi je privolilo v sterilizacijo, a so bili v soglasje najverjetneje prisiljeni, poroča Guardian. Kot razkriva poročilo, je bilo še skoraj 60.000 žensk prisiljenih splaviti zaradi dednih bolezni.

Žrtve in njihovi sorodniki si že leta prizadevajo za razgaljenje diskriminatornega odnosa japonskih oblasti do ljudi s posebnimi potrebami in kroničnimi boleznimi v obdobju po koncu druge svetovne vojne.
Izplačanih le 1049 zahtevkov

Leta 2019 je japonski parlament sprejel zakon, po katerem so vsaki žrtvi ponudili približno 22.800 evrov odškodnine. Predstavniki organizacij za človekove pravice so znesek označili za premajhen. Kot navajajo japonski mediji, se rok za izplačilo odškodnine izteče aprila 2024, doslej pa so jih izplačali le 1049.

Doslej so štiri sodišča odločila, da je treba izplačati odškodnine, druga sodišča pa so zahtevke zavrnila, češ da je že minilo 20-letno obdobje, ko je bilo to mogoče. Odvetniki žrtev so vztrajali, da so bile njihove žrtve o operacijah, ki so jih izvedli na njih, obveščeni prepozno, da bi lahko ujeli zakonske roke.

Podobni zakonodaji sta veljali tudi v Nemčiji in na Švedskem, kjer so se žrtvam opravičili in že izplačali odškodnine.
Prisilna sterilizacija jo je stala zakona in družine

Japonsko sodišče je pretekli mesec zavrnilo zahtevo za izplačilo odškodnine, ki ga je vložila danes 77-lena Junko Iizuka. Pri 16 letih so jo odpeljali na kliniko na severovzhodu države in jo prisilili v neznano operacijo, pozneje se je izkazalo, da so jo sterilizirali. "Ta operacija me je oropala mojih sanj o srečnem zakonu in otrocih." Ko je pozneje odkrila, kaj se ji je zgodilo, je to povedala možu, ta pa jo je zapustil in zahteval ločitev. "Duševno sem zbolela in nisem mogla delati. Diagnosticirali so mi posttravmatski stres. Ta operacija je moje življenje postavila na glavo."

Po objavi poročila se je v imenu vlade državni sekretar v premierjevem uradu Hirokazu Macuno opravičil žrtvam za "nepredstavljivo bolečino," ki so jo utrpele.

"Poročilo ni osvetlilo, zakaj je bil tak zakon sploh sprejet, zakaj je trajalo 48 let, da so ga ukinili, in zakaj žrtve niso nikoli prejele odškodnine," je dejal zastopnik žrtev Koji Nisato.'''
print(len(l))
"""
#v_naslov_datum_url = r'<div class="article-archive-item" date-is="(?P<datum>.+?)">.+?<div class="md-news">.+?<a href="(?P<url>.+?)" class=".+?" title="(?P<naslov>.+?)" tentacle-id="\d+?">'
v_naslov_datum_url = r'<div class="article-archive-item" date-is="(?P<datum>.+?)">.+?<div class="md-news">.+?<a href="(?P<url>.+?)" class=".+?" title="(?P<naslov>.+?)"'
#class="md-news">.+?<a href="(?P<url>.+?)" class=".+?" title="(?P<naslov>.+?)" tentacle-id="\d+?">'
print(os.getcwd())

os.chdir("Arhiv_RTV")
vhod = 'RTV_stran_arhiva_1'
with open(vhod, "r", encoding='utf-8') as v:
    html = v.read()
print(len(html))
a = 0
for n in re.finditer(v_naslov_datum_url, html, flags=re.DOTALL):
    a += 1 
    print(n["naslov"])
print(a)
for vhod in os.listdir():
    with open(vhod, "r", encoding='utf-8') as v:
        html = v.read()
os.chdir("..")
os.chdir("Html_clankov_RTV")
vhod = os.listdir()[3]
with open(vhod, "r", encoding='utf-8') as v:
    html = v.read()
v_cas = r'<div class="publish-meta">(?P<cas>.+?)<'
for najdba in re.finditer(v_cas, html, flags=re.DOTALL):
    cas = najdba["cas"]
    print(cas)"""

print(len("""ODZIV SKUPINE SIJ NA MEDIJSKO POROČANJE

Vodstvo Skupine SIJ v povezavi z zadnjimi medijskimi objavami podaja naslednja pojasnila. 

Vodstvo Skupine SIJ ocenjuje, da gre za politično motivirane objave, usmerjene predvsem v glavnega podpredsednika Skupine SIJ in predsednika Gospodarske zbornice Slovenije Tiborja Šimonko. V imenu največje gospodarske organizacije v Sloveniji kot sogovornik države zagovarja stališča celotnega gospodarstva, del katerega je tudi Skupina SIJ. Tibor Šimonka od prvega dne prevzema mesta predsednika Gospodarske zbornice Slovenije dosledno ločuje obe svoji vlogi, tudi pri podajanju stališč v javnost. Konkretno, GZS je v času energetske krize opozarjala na težave podjetij, na nekonkurenčne pogoje velikih in energetsko intenzivnih podjetij in na cene energentov, ki so v Sloveniji višje kot na konkurenčnih, predvsem tujih trgih. To so dokazljiva dejstva. Vodstvo Skupine SIJ vsebino nekaterih medijskih objav, ki navajajo neuravnotežene in neobjektivne informacije, zato razume predvsem kot opozorila predsedniku gospodarske zbornice, zato podaja naslednja dejstva za razjasnitev vseh okoliščin. 

SIJ d.d., matična družba Skupine SIJ, ni bila prejemnica pomoči. Zato so delničarji skladno s predpisi, pogoji izplačila dividend in zakonom o gospodarskih družbah lahko povsem zakonito izglasovali sklep o izplačilu sicer zakonsko določene minimalne višine dividend. Pravilnost izplačila je v izjavi za N1 13. junija 2023 potrdilo tudi ministrstvo za gospodarstvo, turizem in šport.

Za sprejem te odločitve je bilo na skupščini konec maja na podlagi predloga uprave in nadzornega sveta doseženo popolno soglasje oz. je bilo od udeleženih 967.016 delnic SIJR oddanih 100 odstotkov glasov. Sorazmerni del izplačanih dividend kot lastnica prejme tudi država. Dobički odvisnih družb SIJ Acroni in SIJ Metal Ravne, ki so bili SIJ d.d. izplačani v letu 2022, se nanašajo na dobičke iz poslovanja iz preteklih let in so bili izplačani skladno z zakonodajo. 

SDH, manjšinski lastnik Skupine SIJ, je na svoji spletni strani javno objavil pojasnilo o glasovalnih stališčih v primeru energetske pomoči in dividend. Navedli so kriterije, zaradi katerih SDH v letu 2023 ne bi podprl izplačila dividend. Ker družba SIJ d.d. ni ustrezala tem kriterijem, je izplačilo lahko podprl tudi SDH. 

V zvezi s poslovanjem v letu 2022 in energetsko krizo vodstvo Skupine SIJ pojasnjuje, da je bilo leto 2022 hkrati zaznamovano tako z visokim povpraševanjem po proizvodih kot tudi z visokimi cenami energentov. Upravljanje je terjalo veliko mero fleksibilnosti proizvodnje, kar je bilo v zahtevni jeklarski industriji mogoče zaradi obsežnih preteklih naložb. Sem je sodil tudi začasni ukrep znižanja obsega proizvodnje, ki so jo bili primorani prilagajati tudi visokim cenam električne energije. Stroški energije so bili lani v primerjavi s preteklim letom kljub temu podvojeni. Če se ne bi prilagajali, bi bili vplivi še večji. 

Dobre poslovne rezultate so dosegli tudi zaradi prenašanja višjih vhodnih cen v cene izdelkov za prodajo na svetovnih trgih. Ob tem je Skupina SIJ proizvedla nižje količine kot v letu 2021. Preteklo leto je bilo z vidika okoliščin prej izjema kot pravilo in izjemno kompleksno, zato vodstvo Skupine SIJ naproša, da se v javnosti ne objavljajo posplošene informacije.  

Glede navedb o  visokih plačilih vodstvu skupine in drugih navedb, ki v javnosti želijo ustvariti vtis o siromašenju skupine in njenih družb, navajamo nekaj podatkov iz poslovanja, ki potrjujejo in razvojno-strateško naravnanost lastnikov Skupine SIJ:

- NALOŽBE: Današnji večinski lastnik je v Skupino SIJ vstopil leta 2007. Od takrat do vključno leta 2022 je Skupina SIJ za naložbe namenila 880 milijonov evrov (kar skupaj predstavlja 81 odstotkov EBITDA v obdobju 2007–2022), kar kaže na to, da je večinski lastnik razvojno in strateško naravnan.

- IZPLAČILO DOBIČKA: V šestnajstih letih, odkar ima Skupina SIJ novega lastnika, je trinajst let poslovala z dobičkom. V tem obdobju je ustvarila 279 milijonov evrov dobička. Za dividende je skupaj namenila 94 milijonov evrov (kar predstavlja devet odstotkov EBITDA v obdobju 2007–2022). Preostalih 185 milijonov evrov dobička je ostalo nerazporejenih in namenjenih razvoju podjetja.

- DAVKI: Skupina SIJ je redna plačnica vseh davčnih obveznosti v Republiki Sloveniji. Od leta 2007 je z davki in prispevki v državno blagajno prispevala 283 milijonov evrov.

- STABILEN IN ODGOVOREN DELODAJALEC: V Skupini SIJ je zaposlenih 3.800 sodelavcev. Skupina je s skrbnim upravljanjem in ustrezno obravnavo tveganj, finančno krizo leta 2008, zdravstveno krizo, povezano s koronavirusom, in energetsko krizo premostila brez odpuščanja. Ves čas je redno izplačevala plače, lani pa še dodatne finančne stimulacije za zaposlene. Letos je v proizvodnih družbah v Sloveniji dvignila tudi osnovne plače.

- S POSLUHOM ZA LOKALNO SKUPNOST IN VLAGANJA V DRUŽBO: Skupina je za podporo lokalnim skupnostim od leta 2007 namenila 7,5 milijona evrov, pri čemer se upoštevajo le sredstva iz naslova sponzorstev in don"""))
niz = "<br/>\nGlede navedb o  visokih plačilih vodstvu skupine in drugih navedb, ki v javnosti želijo ustvariti vtis o siromašenju skupine in njenih družb, navajamo nekaj podatkov iz poslovanja, ki potrjujejo in razvojno-strateško naravnanost lastnikov Skupine SIJ:<br/>"

os.chdir("..")
os.chdir("siol")
os.chdir("Clanki_html_SIOL")
vhod = "Html_clanek_528"
with open(vhod, "r", encoding='utf-8') as v:
    html = v.read()
print(len(html))
vzorec = r'<p>(.+?)</p>|<h\d>(.+?)</h\d>|<li>(.+?)</li>|<br/>\n(.+?)<br/>'

for n in re.finditer(vzorec, html, flags=re.DOTALL):
    t = n.group()
    if "SDH, manjšinski" in t:
        print("a")
vz = r'<p>(.+?)</p>|<h\d>(.+?)</h\d>|<li>(.+?)</li>|<br/>\n(.+?)<br/>|<br/>(.+?)<br/>'
niz = "<br/>\nTukaj smo vsi prijatelji.<br/>"
for n in re.finditer(vz, html, flags=re.DOTALL):
    a = n.group()
    if "SDH, manjšinski" in a:
        print(a)
        
print(os.getcwd())
m1 = set()
m2 = set()
for i in range(1,2000):
    dat = f"Html_clanek_{i}"
    with open(dat, "r", encoding='utf-8') as v:
        tek = v.read()
    for najdba in re.finditer(r'<br/>\n(.+?)<br/>', tek, flags=re.DOTALL):
        tt = najdba.group()
        tt = re.sub(r'<.+?>', "", tt)
        tt = tt.strip()
        m1.add(tt)
    for najdba in re.finditer(r'<br/>\n(.+?)<br/>', tek, flags=re.DOTALL):
        tt = najdba.group()
        tt = re.sub(r'<.+?>', "", tt)
        tt = tt.strip()
        m2.add(tt)
print(len(m1&m2)) 
a = sum([len(l) for l in m1&m2]) 

            
        