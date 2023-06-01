from Modules.Utilities import *

def AlegeClasa():
    data = obtineData("clase")
    prescurtari = ['m','a','l']
    while (True):
        raspuns = rpgInput(f"Alege o clasa. [Mag(m)/Luptator(l)/Asasin(a)]")
        if raspuns in prescurtari:
            clasa_index = prescurtari.index(raspuns)
            return convertesteInDictionar(gasesteInData(data, "Prescurtare", raspuns))

def getClasaData(nume):
    data = obtineData("clase")
    clasa = gasesteInData(data, "Clasa", nume)
    return convertesteInDictionar(clasa)

