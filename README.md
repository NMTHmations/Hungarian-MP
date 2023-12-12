# Hungarian MP's wealth statement extracter

(Hungarian version below)

## Introduction

The Hungarian National Assembly's website published the MP's wealth statement, in a more than 2000 pages long document. The document in general not so well readable. To ease accesibility for the Hungarian journalists, or the simple citizens, I have created a tool, which slices the document into several wealth statement document.

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

1. If you want to search by name, you can run this command:

```
python3 searchname.py
```

2. If you want all MPs' wealth statement in a single directory (kepviselok), than you should run this command:

```
python3 pdfextract.py
```

## Limitations

+ Well, the wealth statement documents are not ABC-ordered, so the algorithm's time complexity is much higher, which results long running time.

+ Some politicians may have changed their names, or use different name formats, which the algorithm cannot detect so far. (I'm working on this issue)

+ Search type version will roll out in the next few days. (Solved)

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

1. Ha egy bizonyos képviselőre szeretnél rákeresni, akkor ezt a parancsot futtasd le:

```
python3 searchname.py
```

2. Ha az összes képviselő vagyonnyilatkozatát szeretnéd egy könyvtárban tárolni, akkor ezt a parancsot fusd le:

```
python3 pdfextract.py
```

## Korlátozások

+ Mivel a nagy vagyonnyilatkozati fájl alanyai nem ABC-sorrendben szerepelnek, így az algoritmus időbonyolultsága is nagyobb, ami hosszabb futási időt eredményez.

+ Néhány politikus megváltoztathatta a nevét, vagy más formátumot használ a vagyonnyilatkozatában, mint ahogy a való életben szokott (dolgozok rajta).

+ Keresős változat a következő pár napban várható. (megoldva)
