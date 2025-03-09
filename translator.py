import dictionary
from Parola import Parola
from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dizionario : dictionary = None


    def printMenu(self):
        print("----------------------------\n1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Exit\n")

    def loadDictionary(self, dict):
        self.dizionario = Dictionary(dict)

    def handleAdd(self, entry):
        campi = entry.strip().split(" ")
        parola = Parola(campi[0], campi[1], "Aliena")
        if len(campi) > 2:
            traduzioni = [campi[i] for i in range(2, len(campi))]
            parola.addTraduzioni(traduzioni)
        self.dizionario.addWord(parola)

    def handleTranslate(self, query):
        print(self.dizionario.translate(query))

    def handleWildCard(self,query):
        print(self.dizionario.translateWordWildCard(query))