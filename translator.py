from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dictionary = Dictionary()

    def printMenu(self):
        print(60 * "-")
        print("Translator Alien-Italian")
        print(60 * "-")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print(60 * "-")



    def loadDictionary(self, filename):
        # dict is a string with the filename of the dictionary
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split()

                if len(parts) < 2:
                    continue

                parola_aliena = parts[0].lower()
                traduzioni = [word.lower() for word in parts[1:]]

                self.dictionary.addWord(parola_aliena, traduzioni)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        entry= entry.strip().lower()

        if entry == "":
            print ("Input non valido.")
            return

        parts = entry.split()

        if len(parts) < 2:
            print ("Input non valido.")
            return

        parola_aliena = parts[0]
        traduzioni = parts[1:]

        if not parola_aliena.isalpha():
            print ("Input non valido.")
            return

        for tr in traduzioni:
            if not tr.isalpha():
                print ("Input non valido.")
                return

        self.dictionary.addWord(parola_aliena, traduzioni)
        print ("Parola aggiunta correttamente. Dizionario aggiornato.")


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.strip().lower()
        if query == "":
            print ("Input non valido.")
            return

        if not query.isalpha():
            print("Input non valido.")
            return

        traduzioni = self.dictionary.translate(query)

        if traduzioni is None:
            print ("Parola non trovata.")
        else:
            print("Traduzioni:", ", ".join(traduzioni))

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        query = query.strip().lower()

        if query == "":
            print ("Input non valido.")
            return

        if query.count("?") != 1:
            print ("Input non valido.")
            return

        for ch in query:
            if not (ch.isalpha() or ch == "?"):
                print("Input non valido.")
                return

        risultati = self.dictionary.translateWordWildCard(query)

        if len(risultati) == 0:
            print("Nessuna parola trovata.")
            return

        for parola_aliena in sorted(risultati):
            traduzioni = risultati[parola_aliena]
            print(parola_aliena, "->", ", ".join(traduzioni))

    def handlePrintAll(self):
        all_words = self.dictionary.getAllWords()

        if len(all_words) == 0:
            print ("Dizionario vuoto.")
            return

        for parola_aliena in sorted(all_words):
            traduzioni = all_words[parola_aliena]
            print(parola_aliena, "->", ", ".join(traduzioni))
