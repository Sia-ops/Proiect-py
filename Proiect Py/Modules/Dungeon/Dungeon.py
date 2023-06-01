from Modules.Utilities import *
from Modules.Caracter import EditeazaCaracter
from Modules.Statistici.Stats import *
from random import randint
import math

def Dungeon(caracter):
    rpgPrint("Boohohooo facea fantoma, bafta in pestera", "Pazinc")
    
    data = obtineData("monstri")
    for index, monstru in enumerate(data):
        data[index] = convertesteInDictionar(monstru)

    data.append({
        "Nume": "Boss",
        "HP": 4*getMaxHP(caracter),
        "Putere": randint(math.ceil(1/6*getPutere(caracter)),math.ceil(1/3*getPutere(caracter)))
    })
    pleaca = False
    for monstru in data:
        print("_"*40)
        rpgPrint(f"Te-ai intalnit cu {monstru['Nume']}, pregateste-te de lupta!")
        print(f"HP: {monstru['HP']} | Putere: {monstru['Putere']}")
        while(monstru['HP'] > 0):
            if caracter['Clasa'] != "Asasin": atac(monstru, caracter)
            if caracter['HP'] <= 0:
                pleaca = fugi()
                caracter['HP'] = round(getMaxHP(caracter)/2)
                caracter['Aur'] = round(caracter['Aur']/2)
                print("Ai murit")
                break
            pleaca = tura(caracter, monstru)
            if monstru['HP'] > 0:
                if caracter['Clasa'] == "Asasin": atac(monstru, caracter)
                if caracter['HP'] <= 0:
                    pleaca = fugi()
                    caracter['HP'] = round(getMaxHP(caracter)/2)
                    caracter['Aur'] = round(caracter['Aur']/2)
                    print("Ai murit")
                    break
            else:
                caracter['XP'] += 1
                while(True):
                    raspuns = rpgInput("Ai invins bestia, colecteaza prada(c) sau pregateste-te de urmatorea lupta(v).", caracter['Nume'])
                    match raspuns:
                        case "c":
                            colecteaza(caracter)
                            break
                        case "v":
                            vindeca(caracter)
                            break
                        case "f":
                            pleaca = fugi()
                            break
                        case "h": ajutor()
            if pleaca: break
        if pleaca: break
    
    if(not pleaca):
        rpgPrint("Victorie!!! Ai promovat un nivel.")
        caracter['Nivel'] += 1
        colecteaza(caracter, "boss")
    EditeazaCaracter(caracter)

def tura(caracter, monstru):
    pleaca = False

    if caracter['Mana'] < getMaxMana(caracter): 
        caracter['Mana'] += getManaRegen(caracter)
        if caracter['Mana'] > getMaxMana(caracter): 
            caracter['Mana'] += (getMaxMana(caracter) - caracter['Mana']) #vede cat mana regen ai si iti reumple mana, daca trece peste, scoate surplusul
    
    while (True):
        raspuns = rpgInput("Cum vei ataca bestia?", caracter['Nume']+f"(HP:{caracter['HP']} Mana:{caracter['Mana']})")
        match raspuns:
            case "a": 
                atac(caracter, monstru)
                break
            case "m": 
                magie(caracter, monstru)
                break
            case "f": 
                pleaca = fugi()
                break
            case "h": ajutor()

    return pleaca
    
def atac(atacant, atacat):
    atacuri = obtineData("atacuri")[0] #lista atacuri
    atac_index = randint(0, len(atacuri)-1) #se alege unul la nimereala
    atac = atacuri[atac_index][0]

    if 'Clasa' in atacant.keys(): putere = getPutere(atacant) #vezi daca atacatorul este caracter sau monstru
    else: putere = math.floor(atacant['Putere'] - (atacant['Putere'] * getArmura(atacat)/100)) #regleaza puterea in functie de cata armura ai

    rpgPrint(atacant['Nume']+atac+atacat['Nume']+f" luandu-i {putere} HP") #string care spune ce a atac a fost si cat de puternic
    atacat['HP'] -= putere

def magie(atacant, atacat):
    atacuri = obtineData("magie")[0] #o lista cu atacuri, doar stringuri nu afecteaza cu nimic
    atac_index = randint(0, len(atacuri)-1) #se alege unul din nume la nimereala
    atac = atacuri[atac_index][0]

    putere = getPutere(atacant) + getPutere(atacant) * (atacant['Mana']/100)

    if atacant['Mana'] >= 10: #orice atac magic costa 10 mana
        rpgPrint(atacant['Nume']+atac+atacat['Nume']+f" luandu-i {putere} HP") #string care zice cine cui si cat damage a dat
        atacat['HP'] -= putere #scate viata atacatului
        atacant['Mana'] -= 10 #scade mana atacatorului
    else: rpgPrint("Nu ai destula mana.")

def colecteaza(caracter, monstru = None):
    caracter['Aur'] += 2 * caracter['Nivel'] #monstri normali au 2*level gold
    if monstru == "boss": caracter['Aur'] += 10 * caracter['Nivel'] #bosul da inca 10*level gold

def vindeca(caracter):
    vindeca_standard = 20/100 #mereu primesti 20% din viata lipsa
    vindeca_mana = (caracter['Mana']/caracter['Nivel'])/100 #primesti un procent in funtie de cata mana ai, ex cu 15 mana ai +15%
    vindeca_viata = (getMaxHP(caracter) - caracter['HP']) #asta calculeaza cata viata ai lipsa, procentele de sus arata cat la suta din asta primesti
    caracter['HP'] += math.ceil((vindeca_standard + vindeca_mana)*vindeca_viata) #aici se aduna tot si se adauga la caracter
    if caracter['HP'] > getMaxHP(caracter): caracter['HP'] += getMaxHP(caracter) - caracter['HP'] #daca ai peste viata ta maixima se sterge surplusul

def fugi():
    return True

def ajutor():
    rpgPrint(f"'a' - pentru atac | 'm' - pentru atac magic (extra putere dar costa mana) | 'f' - pentru a fugi | 'c'/'v' - 'c' pentru a colecta bani, 'v' - pentru a va bandaja")

