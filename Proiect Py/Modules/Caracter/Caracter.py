from Modules.Caracter.Clase import AlegeClasa
from Modules.Utilities import *

def CreazaCaracter(nume):
    clasa = AlegeClasa()
    caracter = {"Nume":nume}
    caracter.update({"Clasa":clasa['Clasa']})
    caracter.update({"HP":clasa['HP']})
    caracter.update({"Mana":clasa['Mana']})
    caracter.update({"XP":0})
    caracter.update({"Nivel":1})
    caracter.update({"Aur":10})
    caracter.update({"Coif":"Palarie Mancata de Molii"})
    caracter.update({"Tunica":"Bluza Decolorata"})
    caracter.update({"Nadragi":"Pantaloni Carpiti"})
    caracter.update({"Cizme":"Papuci printre Deget"})
    if caracter['Clasa'] == "Mag": caracter.update({"Sceptru":"Creanga"})
    else : caracter.update({"Sabie":"Tub de Carton"})
    SalveazaCaracter(caracter)
    return caracter

def CautaCaracter(nume):
    data = obtineData("caractere")
    caracter = gasesteInData(data, "Nume", nume)
    return convertesteInDictionar(caracter)

def SalveazaCaracter(caracter, salveaza = True):
    text = f"\nNume={caracter['Nume']}|"
    text += f"XP={caracter['XP']}|"
    text += f"Nivel={caracter['Nivel']}|"
    text += f"Aur={caracter['Aur']}|"
    text += f"Clasa={caracter['Clasa']}|"
    text += f"HP={caracter['HP']}|"
    text += f"Mana={caracter['Mana']}|"
    text += f"Coif={caracter['Coif']}|"
    text += f"Tunica={caracter['Tunica']}|"
    text += f"Nadragi={caracter['Nadragi']}|"
    text += f"Cizme={caracter['Cizme']}|"
    if caracter['Clasa'] == "Mag": text += f"Sceptru={caracter['Sceptru']}|"
    else : text += f"Sabie={caracter['Sabie']}|"
    text += f"Inventar="
    if salveaza:
        open("data/caractere.txt", "a").write(text)
    return text

def EditeazaCaracter(caracter):
    data = obtineData("caractere")
    caracter_vechi = gasesteInData(data, 'Nume', caracter['Nume'])
    caracter_vechi = SalveazaCaracter(convertesteInDictionar(caracter_vechi), False)
    caracter_nou = SalveazaCaracter(caracter, False)
    data = open("data/caractere.txt", "r").read()
    data = data.replace(caracter_vechi, caracter_nou)
    open("data/caractere.txt", "w").write(data)

def AlegeCaracater():
    caracter = None
    while (not caracter):
        raspuns = rpgInput("Continua(c) sau Joc Nou(n)")
        match raspuns:
            case "c": caracter = CaracterExistent()
            case "n": caracter = CaracterNou()
    return caracter

def CaracterNou():
    caractere_nume = gasesteToate(obtineData("caractere"),"Nume")
    nume = rpgInput("Care este numele urmatorului erou?")
    if(nume not in caractere_nume):
        caracter = CreazaCaracter(nume)
        return caracter
    else: rpgPrint(f"{nume} este deja in lupta")
    
def CaracterExistent():
    caractere_nume = gasesteToate(obtineData("caractere"),"Nume")
    nume = rpgInput("Cine s-a intors la misiunea lui de a salva regatul?")
    if(nume in caractere_nume):
        return CautaCaracter(nume)
    else: rpgPrint("Caracterul nu exista!")