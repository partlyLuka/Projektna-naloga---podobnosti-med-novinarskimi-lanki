#testi_za_projektno_nalogo
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time 
import json 
import requests
import datetime

#koda = requests.get("save_page_to_string_selenium(url)")
#print(koda)
#from selenium import webdriver
#from dobi_url import save_string_to_file
#oogleURL = "https://www.rtvslo.si/novice"
#browser = webdriver.Firefox()
#browser.get(googleURL)
#content = browser.page_source
#save_string_to_file(content, "poskus_RTV", "poskus")



start = time.time()
text1 = """
Novak Đoković je v velikem slogu tretjič osvojil Roland Garros in postavil izjemen rekord, saj je v vitrino pospravil že 23. lovoriko na turnirjih za grand slam. V finalu je premagal Casperja Ruuda s 7:6, 6:3 in 7:5 po treh urah in 13 minutah. pariškem pesku. Predal mu ga je Yannick Noah, ki je pred 40 leti osvojil ta turnirpo zmagi nad Matsom Wilandrom. Od takrat že Francozi čakajo na novega junaka. S 23 naslovi ima Srb na večni lestvici eno lovoriko prednosti pred Rafaelom Nadalom. Dvajset jih je osvojil upokojeni Roger Federer. Po osvojenih lovorikah pa se je izenačil z Američanko Sereno Williams, zaostaja pa za Avstralko Margaret Court (24). Ta je sicer le pet let nastopala v odprti eri tenisa, ki se je začela sredi leta 1968.
Ima lepo možnost za koledarski grand slam
Vse turnirje za grand slam je Đoković osvojil najmanj trikrat, kar ni uspelo nobenemu drugemu tenisaču v zgodovini. Na turnirjih velike četverce je dobil zadnjih 21 obračunov, lani v New Yorku ni smel igrati, saj ni predložil potrdila o cepljenju. To pravilo zdaj ni več v veljavi in Beograjčan lahko osvoji tudi koledarski grand slam, ki se mu je izmuznil pred dvema letoma, ko je dobil Melbourne, Pariz in Wimbledon, nato pa je v finalu Odprtega prvenstva ZDA izgubil proti Daniilu Medvedjevu.
Casper Ruud je začel udarno in je po brejku prišel do vodstva s 3:0 v uvodnem nizu, ki pa ga je nato izgubil v podaljšani igri. Foto: Reuters
Casper Ruud je začel udarno in je po brejku prišel do vodstva s 3:0 v uvodnem nizu, ki pa ga je nato izgubil v podaljšani igri. Foto: Reuters
Ruud popustil po vodstvu s 4:1
Prvi je serviral Ruud, ki je gladko s štirimi točkami osvojil prvo igro. Že druga je postregla z maratonsko igro s kar 16 točkami. Đoković je takoj zašel v težave s svojim začetnim udarcem, Norvežan pa je po četrt ure le izkoristil tretjo brejk žogico za vodstvo z 2:0. Sledila je vzpostavitev ravnotežja, ko je v sedmi igri Đoković prišel do prve priložnosti za odvzem servisa. Po izjemni izmenjavi udarcev je Ruud iz bližine poslal žogico v mrežo in Srb je prišel do brejka. Norvežan se je hitro odzval in prišel do priložnosti za rebrejk, a v odločilnih trenutkih je veteran znova potegnil prave poteze in izenačil na 4:4.
Đoković je sijajno odigral podaljšano igro uvodnega niza, ko je oddal le eno točko. V nadaljevanju je bil neustavljiv. Foto: EPA
Đoković je sijajno odigral podaljšano igro uvodnega niza, ko je oddal le eno točko. V nadaljevanju je bil neustavljiv. Foto: EPA
Đoković blestel v podaljšani igri
Po več kot uri igre je odločala podaljšana igra, v kateri pa je Đoković unovčil vse izkušnje in silil Ruuda k neizsiljenim napakam. Tie-break se je končal s kar 7:1 v korist Beograjčana, ki je dobil vseh šest podaljšani iger na letošnjem Roland Garrosu in vse je dobil brez neizsiljene napake.
Srb izjemno serviral v drugem nizu
Prvi niz je trajal kar uro in 23 minut. Đoković je stisnil pest, tudi trener Goran Ivanišević je bil navdušen na tribuni. Srb je zalet presenel v drugi niz. Prvo igro je osvojil brez izgubljene točke. V drugi igri je zapravil tri priložmnosti za brejk, a je unovčil tretjo in nato ekspresno povedel s 3:0. Đoković je izjemno serviral v drugem nizu, v petih igrah na svoj začetni udarec je oddal le pet točk in Ruud je bil nemočen. V osmi igri je še rešil dve priložnosti Srba za zmago v drugem nizu, a je nato Đoković brez izgubljene točke zaključil drugi niz v deveti igri.
Tretji niz je bil znova bolj izenačen, glasno občinstvo pa je skušalo Norvežana ponesti do osvojitve niza in podaljšanja dvoboja. Đoković pa je imel drugačne načrte. V 11. igri je prišel še do tretjega odvzema servisa na dvoboju"""

text2 = """
Srbski zvezdnik Novak Đoković je zmagovalec teniškega odprtega prvenstva Francije v Parizu. V finalu je 36-letni Beograjčan s 7:6 (1), 6:3, 7:5 ugnal Norvežana Casperja Ruuda in osvojil 23. turnir za grand slam v karieri. S tem je zdaj sam na vrhu večne lestvice po naslovih, v ponedeljek pa bo znova prvi igralec sveta.

Izjemni Beograjčan je na Rolandu Garrosu v sedmem finalu slavil tretjič, potem ko je bil najboljši še v letih 2016 in 2021. Pred sedmimi leti je ugnal Britanca Andyja Murrayja, pred dvema pa po preobratu še Grka Stefanosa Cicipasa.

Ob treh naslovih v Parizu je bil Novak Đoković desetkrat najboljši na OP Avstralije, sedemkrat v Wimbledonu in trikrat na OP ZDA. S 23 naslovi ima na večni lestvici eno lovoriko prednosti pred Špancem Rafaelom Nadalom. Dvajset jih je osvojil še upokojeni Švicar Roger Federer.
Za ogled vsebine z družbenih omrežij omogoči piškotke družbenih omrežij.

Đoković je na svojem 70. grand slamu s 34. nastopom v finalu izenačil absolutni rekord Američanke Chris Evert. Po osvojenih lovorikah pa se je izenačil z Američanko Sereno Williams, zaostaja pa za Avstralko Margaret Court (24). Ta je sicer le pet let nastopala v odprti eri tenisa, ki se je začela sredi leta 1968.

Za Norvežana je bil današnji poraz drugi v finalih Rolanda Garrosa in skupno tretji v karieri, potem ko je lani proti Špancu Carlosu Alcarazu izgubil še na zadnji stopnički turnirja v New Yorku. Lani je v finalu Pariza moral priznati premoč Nadalu. V 17. finalu na najvišji ravni je izgubil sedmič.
Za ogled vsebine z družbenih omrežij omogoči piškotke družbenih omrežij.

Đoković se po številu osvojenih turnirjev na najvišji ravni hitro približuje stotici. V 133. finalu je osvojil 94. naslov in se na večni lestvici na tretjem mestu izenačil s Čehom Ivanom Lendlom. Več jih imata le Američan Jimmy Connors (109) in Federer (103). Nadal je na petem mestu z 92.

Po odličnem začetku Ruuda in odvzemu servisa se je Đoković zbral in s tremi zaporednimi igrami izenačil na 4:4. Ruud je v prvem nizu dobil večino daljših izmenjav nad pet udarcev, Đoković pa, ko je do zaključka prišlo prej. Prvi niz je odločila podaljšana igra, v kateri Đoković še šestič na tem turnirju ni napravil niti ene neizsiljene napake. Po sijajni predstavi jo je dobil s 7:1 in povedel z 1:0 v nizih.
Za ogled vsebine z družbenih omrežij omogoči piškotke družbenih omrežij.

V drugem je na krilih osvojenega prvega niza takoj odvzel servis 12 let mlajšemu Norvežanu in brez večjih težav povedel z 2:0 v nizih. Tretji niz je bil znova bolj izenačen, glasno občinstvo pa je skušalo Norvežana ponesti do osvojitve niza in podaljšanja dvoboja. Đoković pa je imel drugačne načrte. V 11. igri je prišel še do tretjega odvzema servisa na dvoboju in ga zanesljivo končal po treh urah in 13 minutah."""

text3 = """


Novak Đoković je zmagovalec teniškega OP Francije, potem ko je v finalu premagal Norvežana Casperja Ruuda (7:6 (1), 6:3, 7:5). Srbski teniški zvezdnik se je s to zmago vpisal v zgodovino tenisa, potem ko je postal igralec z največ osvojenimi turnirji za grand slam. Nole jih ima trenutno v svoji vitrini 23.
 
Novak Đoković
Sportal
Pri Đokoviću spet nekaj ugibanj, bo zdržal?

Đoković, ki je v Parizu slavil še tretjič v karieri, je na Roland Garrosu dosegel še en mejnik. S 36 leti je namreč postal najstarejši igralec, ki je slavil na najprestižnejšem turnirju na pesku. Poleg tega pa se bo z naslednjim tednom vrnil na sam vrh svetovne lestvice ATP. Dvoboj se je končal po treh urah in 16 minutah.

Casper Ruud je bil še najbolj konkurenčen v prvem nizu, ko je imel vse možnosti, da povede z 1:0  nizih. Od prvega niza dalje pa je več ali manj vse niti v rokah zdaj že 23-kratni zmagovalec turnirjev za grand slam.

Novak Đoković , Casper Ruud | Foto: Guliverimage Foto: Guliverimage

Kot pravi športnik, je Novak Đoković najprej nekaj besed namenil svojem nasprotniku v finalu, Casperju Ruudu. Norvežan ga je že nekaj trenutkov pohvalil in Srbu čestital za vse besede.

"Casper, hvala za tvoje lepe besede. Ne samo zato, ker stojiva tukaj, ampak si ena najboljših oseb na turneji. Vsi na turneji te imajo radi in te spoštujejo. To sem moral najprej povedati, ker res čutim, da je v današnjem svetu zelo pomembno, da immo človeške vrednote. Ti in vsi v tvoji ekipi so vedno zelo prijazni do mene. Vsi si zaslužite veliko spoštovanje. Žal mi je za izid, ki se danes ni izšel po tvojih željah," je uvodoma povedal Đoković, potem pa se obrnil k svoji ekipi in jih nagovoril z izbranimi besedami.

Novak Đoković | Foto: Guliverimage Foto: Guliverimage
Ljudje ne vedo, kaj se dogaja za zaprtimi vrati

"Moja ekipa, družina, moja dva brata, ki trenutno nista tukaj, a jih imam zelo rad … Ne vem, kaj naj rečem. Vsi vemo, skozi kaj smo šli. Vi veste, kako težko je dnevno delati z mano. Kot prvo, bi se vam rad zahvalil za vaše potrpljenje. Vemo, kaj sem vam delal v zadnjih tednih. Ljudje tega ne vedo, ampak za zaprtimi vrati, sem vas "mučil". Vi ste moja podpora, verjamete vame in to res cenim. Res sem vam hvaležen ," je na slavnostni podelitvi povedal Đoković.

Casper Ruud je že v drugi igri uvodnega niza naredil "break". | Foto: Guliverimage Casper Ruud je že v drugi igri uvodnega niza naredil "break". Foto: Guliverimage Novak se je po začetnih težavah vrnil in dobil uvodni niz

Uvodno igro dvoboja je začel Casper Ruud, ki jo je dobil brez izgubljene točke in povedel z 1:0. Đoković je imel s prvo igro na svoj servis veliko več težav. Norvežan si je ustvaril dve žogici za "break", a ju sprva ni uspel izkoristiti. Mu je pa zato uspelo v tretje in povedel z 2:0. Ruud je v naslednji igri potrdil odvzem servisa in povedel že s 3:0. Srb se je prvič na rezultatsko tabelo vpisal v četrti igri, ko je zaostanek znižal na 1:3.

Med igro smo lahko slišali huronsko vzklikanje: Nole, Nole, … Občinstvo je bilo na njegovi strani. V sedmi igri si je Đoković ustvaril prvo žogico za odvzem servisa. Po izjemno dolgi izmenjavi jo je uspel izkoristiti in izničil zaostanek "breaka". V naslednji igri je na svoj servis že izenačil na 4:4. Prvi niz je odločila podaljšana igra. Tam je več zbranosti in kakovosti pokazal Đoković in po skoraj uri in pol (1:22) dobil prvi niz (7:6 (1).

Novak Đoković je v prvem nizu sodniku dopovedoval, da naj pusti več časa za počitek. | Foto: Guliverimage Novak Đoković je v prvem nizu sodniku dopovedoval, da naj pusti več časa za počitek. Foto: Guliverimage
Razprava s sodnikom

Đoković je imel v prvem nizu tudi razgovor s sodnikom. Srba je zmotilo, da prehitro vklopi uro za odmor. "Za božjo voljo, ne vidiš, da niz traja več kot eno uro. Daj nam čas za počitek," se je pritoževal Nole.

Novak Đoković je ob koncu prvega niza našel pravi ritem in dvignil raven svoje igre. | Foto: Guliverimage Novak Đoković je ob koncu prvega niza našel pravi ritem in dvignil raven svoje igre. Foto: Guliverimage
Srb je bil v drugem nizu veliko bolj razpoložen

Srbski teniški zvezdnik je drugi niz začel veliko bolje, saj je v prvo igro dobil brez izgubljene točke in na hitro povedel z 1:0. Đoković je v tem stilu tudi nadaljeval, saj je nasprotniku že v drugi igri vzel servis in povedel z 2:0. V naslednji igri je imel eden najboljših igralcev vseh časov v rokah vodstvo s 3:0. V četrti igri je Ruud dobil svojo prvo igro in znižal izid na 1:3.

V nadaljevanju niza nismo več videli večjih preobratov. V osmi igri je imel sicer Novak že dve žogici za drugi niz, a se je Norvežan uspel vrniti in rezultat znižal na 3:5. Zato pa je Đokovič svoje delo opravil v deveti igri, ki jo je dobil brez težav in povedel z 2:0 v nizih. Drugi niz se je končal z izidom 6:3 in je trajal 52 minut.

Casper Ruud | Foto: Guliverimage Casper Ruud Foto: Guliverimage
Tretji niz je odločila enajsta igra

Tretji niz se je začel bolj izenačeno. Oba igralca sta brez težav dobila uvodni igri na svoj servis. V tretji igri je Beograjčan prišel do prve žogice za odvzem servisa, a je ni uspel izkoristiti. Ruud je pozneje dobil to igro in povedel z 2:1. V četrti igri je imel Đoković veliko manj dela, da je izenačil na 2:2, saj nasprotniku ni oddal niti ene točke.

V osmi igri smo lahko slišali vzklikanje ime Norvežana, potem ko je povedel z 0:30. Veselje norveških navijačev ni trajalo dolgo, saj je Đoković kmalu izenačil na 30:30, pozneje pa dobil igro in izenačil na 4:4. Tik pred tem je od sodnika dobil opozorilo zaradi velika premora med točkama, kar je razburilo srbske navijače na tribunah.

Novak Đoković je po zadnji točki obležal na pesku. | Foto: Guliverimage Novak Đoković je po zadnji točki obležal na pesku. Foto: Guliverimage

Nato je prišla na vrsto enajsta igra, ko je Srbu uspelo nekaj izjemnih udarcev in na servis Ruuda povedel z 0:40 in si priigral tri žogice za "break". Izkoristil je že prvo in povedel s 6:5. Dvanajsta igra je bila za izkušenega Đokovića le še formalnost, ki je po zadnji točki obležal na igrišču in se s tem"""


vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([text1, text2, text3])

#similarity = cosine_similarity(vectors)
end = time.time()
import enchant
  
# determining the values of the parameters
string1 = "Dokovič o novi sezoni"
string2 = "Nocak Dokovič si želi novih izzivov."
  
# the Levenshtein distance between
# string1 and string2
print(enchant.utils.levenshtein(string1, string2))

print(end - start  )

urlji = []
#f'https://siol.net/pregled-dneva/2023-{a}-{b}/'
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(365)]
dates = [(x.year, x.month, x.day) for x in date_list]
print(len(dates))

urlji_arhiva = [f'https://siol.net/pregled-dneva/{x[0]}-{x[1]}-{x[2]}/' for x in dates ]
for k in urlji_arhiva:
    print(k)
s = {1:(2,3,5), 2:(5,3,1)}
with open("Test.json", "w", encoding = 'utf-8') as dat:
    json.dump(s, dat)
