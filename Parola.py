class Parola:
    def __init__(self, parola, traduzioni, lingua):
        self.lingua = lingua
        self.parola = parola
        self.traduzioni = []
        self.traduzioni.append(traduzioni)

    def addTraduzioni(self, traduzioni):
        self.traduzioni.extend(traduzioni)

    def translate(self):
        traduzione = ""
        for trad in self.traduzioni:
            if traduzione != "":
                traduzione += " "
            traduzione += trad
        return traduzione