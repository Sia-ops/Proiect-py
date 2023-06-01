def filtreazaData(data, categorie, valoare):
    values = []
    for vector in data:
        for element in vector:
            if (categorie in element):
                if (valoare in element[1]):
                    values.append(vector)
                    continue
                try:
                    if (element[1] in valoare):
                        values.append(vector)
                except:
                    pass
    return values