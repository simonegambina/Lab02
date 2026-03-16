import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")


while True:
    t.printMenu()
    txtIn = input().strip()

    # Add input control here!

    if not txtIn.isdigit():
        print ("Scelta non valida. Inserisci un numero da 1 a 5.")
        continue

    choice = int(txtIn)

    if choice < 1 or choice > 5:
        print("Scelta non valida. Inserisci un numero da 1 a 5.")
        continue

    if choice == 1:
        print ("Inserisci la nuova entry: ")
        entry = input()
        t.handleAdd(entry)

    elif choice == 2:
        print ("Inserisci la parola da tradurre: ")
        query = input()
        t.handleTranslate(query)

    elif choice == 3:
        print("Inserisci la tua parola con wildcard '?':")
        query = input()
        t.handleWildCard(query)

    elif choice == 4:
        t.handlePrintAll()

    elif choice == 5:
        print("Arrivederci!")
        break





