from Modules.Utilities import *
from Modules.Caracter.Clase import getClasaData

def printStats(caracter):
    tiparma = ""
    if caracter['Clasa'] == "Mag": tiparma = "Sceptru"
    else: tiparma = "Sabie"
    rpgPrint("Statistici\n"
             f"{caracter['Nume']} (XP:{caracter['XP']}) Aur: {caracter['Aur']}\n"
             f"HP: {caracter['HP']}/{getMaxHP(caracter)} | Mana: {caracter['Mana']}/{getMaxMana(caracter)}\n"
             f"Coif: {lungimePerfecta(30, caracter['Coif'])}   Arma: {caracter[tiparma]}\n"
             f"Tunica: {lungimePerfecta(30, caracter['Tunica'])} Putere: {getPutere(caracter)}\n"
             f"Nadragi: {lungimePerfecta(30, caracter['Nadragi'])}Armura: {getArmura(caracter)}\n"
             f"Cizme: {lungimePerfecta(30, caracter['Cizme'])}  Mana Rgen: {getManaRegen(caracter)}")
    
def getArmuraData(caracter, armura):
    data = obtineData("armuri")
    return convertesteInDictionar(gasesteInData(data, "Nume", caracter[armura]))
def getArmaData(caracter, arma):
    data = obtineData("arme")
    return convertesteInDictionar(gasesteInData(data, "Nume", caracter[arma]))

def getArmura(caracter):
    armura = getArmuraData(caracter, "Coif")['Armura']
    armura += getArmuraData(caracter, "Tunica")['Armura']
    armura += getArmuraData(caracter, "Nadragi")['Armura']
    armura += getArmuraData(caracter, "Cizme")['Armura']
    return armura

def getManaRegen(caracter):
    mana = getClasaData(caracter['Clasa'])['ManaRegen']
    mana += getArmuraData(caracter, "Coif")['ManaRegen']
    mana += getArmuraData(caracter, "Tunica")['ManaRegen']
    mana += getArmuraData(caracter, "Nadragi")['ManaRegen']
    mana += getArmuraData(caracter, "Cizme")['ManaRegen']
    return mana

def getMaxHP(caracter):
    hp = getClasaData(caracter['Clasa'])['HP']
    hp += getArmuraData(caracter, "Coif")['HP']
    hp += getArmuraData(caracter, "Tunica")['HP']
    hp += getArmuraData(caracter, "Nadragi")['HP']
    hp += getArmuraData(caracter, "Cizme")['HP']
    return hp

def getMaxMana(caracter):
    Mana = getClasaData(caracter['Clasa'])['Mana']
    Mana += getArmuraData(caracter, "Coif")['Mana']
    Mana += getArmuraData(caracter, "Tunica")['Mana']
    Mana += getArmuraData(caracter, "Nadragi")['Mana']
    Mana += getArmuraData(caracter, "Cizme")['Mana']
    return Mana

def getPutere(caracter):
    putere = getClasaData(caracter['Clasa'])['Putere']
    if caracter['Clasa'] == "Mag": arma = "Sceptru"
    else: arma = "Sabie"
    putere += getArmaData(caracter, arma)['Putere']
    return putere