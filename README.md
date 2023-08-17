# Projektna-naloga---podobnosti-med-novinarskimi-lanki
Raziskava, kako podobni so si članki, ki so objavljeni na RTV in Siolu. 
S sledečim projektom smo odgovorili na sledeča vprašanja:
* Ali so članki, ki so objavljeni na RTV bolj podobni Siolovim člankom, kot so Siolovi članki podobni člankom iz RTV?
* Ali je moč sumiti na kakršnokoli plagiatstvo med medijskima hišama?
* Ali se povprešna podobnost člankov iz ene medijske hiše spreminja s časom?
Najprej moramo razjasniti, kaj pomeni beseda _podoben_. Ideja je v tem, da izračunamo kot med dvema tekstovnima datotekama in na podlagi tega rezultata
presodimo, ali sta si v nekem smislu sorodna. V ta namen smo uporabili knjižnico scikit learn, bolj natančno funkcijo cosine_similarity. Funkcija sprejme dve besedili in vrne vrednost med
-1 in 1 (kosinus kota med besedili). Če je rezultat blizu 1, pomeni, da je kot blizu 0, kar pomeni, da sta si besedili podobni. Nasprotno - če je rezultat blizu -1, implicira, da sta si besedili ravno nasprotni.
Večina kode je posvečena zajemu besedil. Postopek je potekal nekoliko takole:
* Naložili smo html datoteke strani arhivov in iz njih izluščili url do dejanskih člankov
* Naložili smo html datoteke člankov ter nato izluščili vsebino članka ter nekatere pomembne informacije (avtor članka, čas objave...)
* Besedila smo prepisali v txt datoteke
Tako smo naložili članke iz obeh medijskih hiš, ki so bili objavljeni v zadnjem letu. Nabralo se je okolo 55.000 člankov.
Naposled koda sledi dejanskim izračunom. Tu smo za vsak članek preverili, ali je nemara plod plagiatstva. To smo naredili tako, da smo za sleherni članek poiskali članek, ki je imel največjo
kosinusno podobnost in je hkrati bil objavljen največ 3 dni pred obravnavanim člankom. V resnici smo poiskali tri najpodobnejše članke, a smo uporabili podatek, ki se navezuje na najpodobnejšega.
Poleg tega smo še izračunali Levenshteinovo razdaljo med obravnavanim člankom in njemu najpodobnejšim člankom. To je razdalja med dvema nizoma str1 in str2, ki pove, koliko je najmanj potrebnih menjav, da
str1 spremenimo v str2.
V zadnjem dokumentu smo vse povezali in predstavili v jupyter notebooku.  
V mapi "testi" so shranjene kode, katerih kardinalni smoter je pridobiti vsebino člankov iz RTV.
Mapa "siol" je namenjena pridobitvi vsebine člankov izi Siola.
Mapa "korelacije" je posvečena konkretnim računom kosinusnih podobnostih in zadnje priprave na analizo podatkov.
V mapi "analiza_podatkov" pa seveda izvedemo končno analizo podatkov in predstavimo rezultate.
Opomba: v repository nismo shranili tekstovnih datotek, v katerih je zapisana vsebina člankov, saj je teh preprosto preveč. Bistveni podatki (podobnosti, itd.) so shranjeni v CSV datotekah v mapi "analiza_podatkov". 
