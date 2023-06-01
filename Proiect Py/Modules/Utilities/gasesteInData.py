#functie care gaseste elemente din fiesere text obtinute cu getData.py

def gasesteInData(data, field, value):
    for vector in data: #loop care merge prin toate sublistele din "data"
        for element in vector: #loop care merge prin toate elementele din subliste
            if (field in element): #verifica daca subelementul actual este cel cautat
                if (value in element[1]): #verifica daca valoarea din subelementul actual este egala cu cea cautata
                    return vector #returneaza lista dorita
                
#ex gasesteInData(obtineData("Caractere"), "Nume", "Andreea")
#va cauta in data obtinuta din fisierul Caractere lista care are la pozitia "Nume" valoarea "Andreea"