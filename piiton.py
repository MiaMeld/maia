from easygui import *

def loe_fail(failinimi):
    try:
        with open(failinimi, encoding='UTF-8') as f:
            return f.readlines()
    except FileNotFoundError:
        msgbox("Faili ei leitud!", "Viga")
        return None

def kirjuta_fail(failinimi, sisu):
    with open(failinimi, 'w', encoding='UTF-8') as f:
        f.write(sisu)

def loe_ja_naita_faili_sisu(failinimi):
    sisu = loe_fail(failinimi)
    if sisu:
        msgbox("Faili sisu:\n\n" + ''.join(sisu), "Faili sisu")
        
def displaycontent(content):
    sisu2 = ""
    for rida in content:
        sisu2 += (rida.strip() + "\n")
    msgbox(sisu2)

while True:
    valik = buttonbox("Mida soovid teha?", choices=["Loo 'kaka' fail", "Loe 'kaka' faili", "Loe faili", "Lõpeta"])
    
    if valik == "Loo 'kaka' fail":
        failinimi = filesavebox("Salvesta fail nimega:")
        if failinimi:
            kirjuta_fail(failinimi, "kaka")
            msgbox("Fail 'kaka' loodud ja salvestatud!", "Edu")
    
    elif valik == "Loe 'kaka' faili":
        sisu3 = open("kaka1.txt", encoding="UTF-8")
        content = sisu3.readlines()
        sisu3.close()
        displaycontent(content)
        
    
    elif valik == "Loe faili":
        failinimi = fileopenbox("Ava fail:")
        if failinimi:
            loe_ja_naita_faili_sisu(failinimi)
    
    elif valik == "Lõpeta":
        break