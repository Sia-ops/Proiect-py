from Modules.Caracter import AlegeCaracater
from Modules.Statistici.Stats import printStats
from Modules.Taverna import Taverna
from Modules.Dungeon import Dungeon


functii = { "s": printStats, "t": Taverna , "d": Dungeon} #dictionar ce contine functiile care pot fi apelate de utiliztor 

def actiune(): #functie care cere un input de utilizator, daca inputul se potrivieste cu unul din elementele dictionarul, functia respecteviva din dictionar este apelata
    actiune = input(f"\n{caracter['Nume']}: ").lower() #input
    if actiune in functii: functii[actiune](caracter) #verifica daca este in dictionar + apeleaza functia
    elif actiune == "iesi": quit() #inchide jocul la inputul "iesi"

caracter = AlegeCaracater() #apeleaza functia importata din modulul Caracter
print("'s' - statistici | 't' - taverna | 'd' - dungeon")
while(True): actiune() #loop infinit care apeleaza functia "actiune"