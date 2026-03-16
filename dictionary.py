class Dictionary:
    def __init__(self):
        self.words = {}

    def addWord(self, parola_aliena, traduzioni):
        if parola_aliena not in self.words:
            self.words[parola_aliena] = []
        for tr in traduzioni:
            if tr not in self.words[parola_aliena]:
                self.words[parola_aliena].append(tr)


    def translate(self, query):
        if query in self.words:
            return self.words[query]
        return None

    def translateWordWildCard(self, query):
        risultati = {}

        for parola_aliena in self.words:
            if len(parola_aliena) != len(query):
                continue

            match = True

            for i in range(len(query)):
                if query[i] != "?" and query[i] != parola_aliena[i]:
                    match = False
                    break

            if match:
                risultati[parola_aliena] = self.words[parola_aliena]

        return risultati

    def getAllWords(self):
        return self.words