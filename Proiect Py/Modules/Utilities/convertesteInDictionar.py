def convertesteInDictionar(data):
    dictionar = dict()
    for element in data:
        if isinstance(element[1], list):
            dictionar.update({element[0]:element[1]})
        elif element[1].isnumeric():
            dictionar.update({element[0]:int(element[1])})
        else:
            dictionar.update({element[0]:element[1]})
    return dictionar