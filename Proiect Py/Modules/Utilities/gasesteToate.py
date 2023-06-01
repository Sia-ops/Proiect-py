#functie care returneaza toate vaolirle aceeasi chei

def gasesteToate(data, field):
    valori = [] #vector ce va stoca valorile
    for vector in data: #loop care merge prin toate sublistele din "data"
        for element in vector: #loop care merge prin toate elementele din subliste
            if (field in element): #verifica daca subelementul actual este cel cautat
                valori.append(element[1]) #adauga valoarea actuala in vectorul "valori"
    return valori

#ex poti folosi aceasta functie sa gasesti toate numele din fisierul Caractere sau toate punctele XP, etc