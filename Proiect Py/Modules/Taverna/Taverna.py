from Modules.Utilities import *
from Modules.Caracter import EditeazaCaracter

def Taverna(caracter):
    rpgPrint("Ce vant te aduce pe aici?", "Fierar")
    while(True):
        raspuns = rpgInput("Vrei arme(a) sau platosa(p)? (Inapoi la meniu(i))", caracter['Nume'], "Fierar")
        match raspuns:
            case 'a': gasesteProduse(caracter, "arme")
            case 'p': gasesteProduse(caracter, "armuri")
            case 'i': 
                rpgPrint("Sa-ti frangi gatul si picioarele", "Fierar")
                break

def gasesteProduse(caracter, categorie):
    date = obtineData(categorie)
    produse = filtreazaData(date, "Nivel", str(range(1,caracter['Nivel']))) #pastreaza doar produsele care sunt de acelasi level sau mai mic decat al jucatorului
    produse = filtreazaData(produse, "Clasa", caracter['Clasa'])#pastreaza daor produsele din aceeasi clasa cu utilizatorul

    for index, produs in enumerate(produse): produse[index] = convertesteInDictionar(produs) #converteste toate listele din data in dictionare

    rpgPrint(f"Sa vedem ce {categorie} avem.\n"+("_"*50)+"\n", "Fierar")
    produse_nume = dict() 
    for produs in produse: #creeaza un dictionar in care avem ca si cheie numele produselor si ca si valoare un dictionar cu atributele produselor
        produse_nume.update({produs['Nume'].lower():produs})
        printProdus(produs, categorie)
    cumparaProdus(caracter, produse_nume)

def printProdus(produs, categorie): #printeaza atributele
    print(
            f"\n--{produs['Nume']}--[{produs['Tip']}]\n"
            f"Pret: {produs['Pret']}.gold"
        )    
    if categorie == "arme":
        print(f"Putere: {produs['Putere']}\n")
    elif categorie == "armuri": 
        print(
            f"Armura: {produs['Armura']}\n"
            f"HP: {produs['HP']}\n"
            f"Mana: {produs['Mana']}\n"
            f"Mana Regen: {produs['ManaRegen']}\n"
        )
    print("-"*20)

def cumparaProdus(caracter, produse): #verifica daca numele introdus de utilizator apartine unui produs. Daca da scade suma de bani de la utilizator si ii "vinde" produsul
    while(True):
        raspuns = rpgInput("Introdu nume",  caracter['Nume'], "Fierar")
        if raspuns in produse:
            if caracter['Aur'] < produse[raspuns]['Pret'] : 
                rpgPrint("Sufla vantul prin portofel", "Fierar")
                break
            
            caracter[produse[raspuns]['Tip']] = produse[raspuns]['Nume']
            caracter['Aur'] -= produse[raspuns]['Pret']

            rpgPrint("Hehe, ti-am cerut pret dublu", "Fierar")
            EditeazaCaracter(caracter)
            break
        elif raspuns == "i": break