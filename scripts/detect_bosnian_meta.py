#!/usr/bin/env python3
"""Detect EN/DE pages with Bosnian titles/descriptions for translation."""
import os, re

ROOT = "/root/bixie-site"
BOSNIAN_WORDS = ["kako", "vasa", "vase", "vasoj", "vasi", "vasu", "vasem", "koji", "koliko",
    "ustedio", "povecala", "smanjila", "rjesenja", "provajderi", "buducnost", "vodic", "agenti",
    "signali", "pravog", "pomazu", "lead", "implementirati", "automatizirati", "sta", "nakon",
    "kroz", "sistem", "obrada", "zdravstvo", "racunovodstvo", "nabavke", "trijaza", "skladiste",
    "pumpi", "logisticka", "bolnica", "advokatska", "osiguravajuca", "proizvodna", "obrazovanju",
    "upravljanje", "ljudske", "morate", "chatbotovi", "kljucne", "poredjenje", "trendova",
    "prelaze", "velike", "korisnicku", "korisnicke", "praktican", "prakse", "potpuni", "evropski",
    "konkurira", "rekorde", "promijeniti", "pripremiti", "odabrati", "cuvanju", "pretrazi",
    "funkcionisu", "efikasniji", "slozene", "napusta", "razloge", "nezavisnost", "uskaldjivanju",
    "pravna", "autonomni", "konverziju", "smanjuju", "segmentacije", "personalizacije",
    "zadovoljstvo", "regrutacije", "onboardinga", "performansama", "detaljan", "hardverski",
    "hardveru", "preduzimaju", "umjesto", "godisnje", "zaposlenih", "finansijskih", "povecao",
    "koristeci", "prodajnog", "savjeti", "predvidanja", "optimizacija", "kontaktirajte",
    "posaljite", "zakazite", "male firme", "cesto", "uslove", "koristenja", "javne", "uprave",
    "transparentnost", "efikasnost", "troskova", "sigurnost", "skole", "univerzitete",
    "akademskim", "cijenama", "skolskoj", "personalizovano", "ucenje", "banke", "institucije",
    "rizika", "prevara", "privatnost", "odrzavanje", "vizuelna", "inspekcija", "predvidjanje",
    "personalizovane", "ponude", "podrsku", "podrske", "troskove", "uvodjenja", "smanjivsi",
    "benchmarkovi", "kvantizacija", "zahtjevi", "produkcijsku", "upotrebu", "primjeri",
    "izvjestaji", "anomalija", "finansijski", "sektor", "izvjestaja", "visejezicnost", "rusi",
    "slucajeve", "slucajevi", "poredjenje", "vodic", "gdje", "zasto", "trebate", "sve", "sto",
    "znate", "vasem", "poslovanju", "potencijalnih", "klijenata", "strategije", "najbolje",
    "prilagodjen", "potrebama", "tipova", "cijena", "funkcionalnosti", "organizaciji", "cuvanju",
    "pretrazi", "poslovnog", "znanja", "slozenih", "rjesenja", "zadataka", "ustanova", "nastavnicima",
    "administrativne", "zadatke", "koristi"]

def is_bosnian(text):
    t = text.lower()
    if re.search(r'[čćšžđ]', t):
        return True
    for w in BOSNIAN_WORDS:
        if w in t:
            return True
    return False

for base in ("en", "de"):
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, base)):
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dirpath, fn)
            html = open(p, encoding="utf-8").read()
            t = re.search(r'<title>(.*?)</title>', html, re.S)
            d = re.search(r'<meta property="og:description" content="([^"]*)"', html)
            title = t.group(1).strip() if t else ""
            desc = d.group(1).strip() if d else ""
            if is_bosnian(title) or is_bosnian(desc):
                rel = os.path.relpath(p, ROOT)
                flag = []
                if is_bosnian(title): flag.append("T")
                if is_bosnian(desc): flag.append("D")
                print(f"{rel}|{','.join(flag)}|{title[:70]}|{desc[:90]}")
