from Parola import Parola


class Dictionary:
    def __init__(self, filename):
        self.parole = []
        with open(filename, "r") as file:
            for line in file:
                campi = line.lower().strip().split(" ")
                parola = Parola(campi[0], campi[1], "Alieno")
                self.parole.append(parola)
                parola = Parola(campi[1], campi[0], "Italiano")
                self.parole.append(parola)


    def addWord(self, parola):
        self.parole.append(parola)

    def translate(self, query):
        for parola in self.parole:
            if parola.parola == query:
                return parola.translate()

    def translateWordWildCard(self, query):
        campi = query.lower().strip().split("?")
        for parola in self.parole:
            if parola.parola.startswith(campi[0]) and parola.parola.endswith(campi[1]):
                return parola.translate()