# Hungarian MP's wealth statement extracter

(Hungarian version below)

## Introduction

The Hungarian National Assembly's website published the MP's wealth statement, in a more than 2000 pages long document. The document in general not so well readable. To ease accesibilitz for the Hungarian journalists, or the simple citizens, I have created a tool, which slices the document into several wealth statement document.

## Installation, settings

In order to use the script, you have to download Python 3.x, from the [developer's website](https://www.python.org/downloads/).

Than you have to install the following packages with pip3:

```
pip3 install beautifulsoup4
pip3 install requests
pip3 install regex
pip3 install PyPDF2
```

## Usage

Once You have downloaded python, and all the packages, then you can use the extracter tool.

To avoid crashes, I recommend the following steps, in order to maintain your MP's wealth statements:

1. Use names_to_csv.py, with the following command:

```
python3 names_to_csv.py
```

2. Than run the pdfextract.py, with this command:

```
python3 pdfextract.py
```

## Limitations

+ Well, the wealth statement documents are not ABC-ordered, so the algorithm's time complexity is much higher, which results long running time.

+ Some politicians may have changed their names, or use different name formats, which the algorithm cannot detect so far. (I'm working on this issue)

+ Search type version will roll out in the next few days.

# Vagyonnyilatkozat-szeletelő

## Bevezetés

A magyar parlament a napokban publikálta a képviselők vagyonnyilatkozatait egy több mint 2000 oldalas dokumentumban. A dokumentum így alapjában véve nem túl jól olvasható. Hogy könnyítsük a magyar újságírók, és állampolgárok számára a hozzáférhetőséget, ezért csináltam egy eszközt, ami "szétszeleteli" a dokumentumot több kisebb dokumentumra (képviselők szerint).

## Telepítés, beállítás

Ahhoz hogy a szkriptet megfelelően tudjuk használni, ahhoz szükséges a Python 3.x legfrisebb verziójának a letöltése a [fejlesztők oldaláról](https://www.python.org/downloads/).

Ezután a pip3 csomagkezelőt használva ezeket kell feltelepítened parancssorból:

```
pip3 install beautifulsoup4
pip3 install requests
pip3 install regex
pip3 install PyPDF2
```

## Használat

Ha már telepítetted a Pythont, és az összes szükséges csomagot, akkor már használhatod a "szeletelő" eszközt.

Hogy elkerüld a hibákat, összeomlásokat, ehhez én a következő parancsokat (és annak sorrendet) ajánlom:

1. Futtasd a names_to_csv.py fájlt parancssorból így:

```
python3 names_to_csv.py
```

2. És ezután futttasd a pdfextract.py-t a következő paranccsal:

```
python3 pdfextract.py
```

## Korlátozások

+ Mivel a nagy vagyonnyilatkozati fájl alanyai nem ABC-sorrendben szerepelnek, így az algoritmus időbonyolultsága is nagyobb, ami hosszabb futási időt eredményez.

+ Néhány politikus megváltoztathatta a nevét, vagy más formátumot használ a vagyonnyilatkozatában, mint ahogy a való életben szokott (dolgozok rajta).

+ Keresős változat a következő pár napban várható.