#funtie folosita pentru a extrage date din fisiserele text

def obtineData(locatie):
    data = open(f"data/{locatie}.txt", "r").read().splitlines() #fiecare linie din fisierul text este salvata ca o lista intr-o alta lista numita "data"
    for index, vector in enumerate(data): #loop care trece prin elementelei listei "data" 
        data[index] = vector.split("|")  # fiecare lista este impartita in elemente
        for pozitie, element in enumerate(data[index]): #loop care trece prin toate elementele
            data[index][pozitie] = element.split("=") #fiecare element est impartit in subelemente
            for contor, subelement in enumerate(data[index][pozitie]):
                if("+" in subelement): data[index][pozitie][contor] = subelement.split("+")
    return data

#fiecare element/caracter/monstru sunt salvate in fisiere txt si scrise pe o linie
#sunt salvate sub forma de cheie si valoare (ex Nume=sia)
#intre cheie si valoare este un "="
#perechile de chei si valori sunt despartite prin "|" (ex Nume=sia|HP=10)
#unele valori au mai multe elemente, acestea sunt despartite prin "+" (ex Clasa=Asasasin+Luptator)