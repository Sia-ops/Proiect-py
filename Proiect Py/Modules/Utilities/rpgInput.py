def rpgInput(text, caracter = "Jucator", joc = "Joc"):
    print(f"\n>{joc}: {text}")
    raspuns = input(f"{caracter}: ").lower()
    if raspuns == "iesi": quit()
    return raspuns