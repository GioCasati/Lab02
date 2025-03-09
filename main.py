import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while True:
    t.printMenu()
    txtIn = input("Scegli: ")
    go = txtIn.isdigit() and 5 > int(txtIn) > 0
    while not go:
        txtIn = input("Scegli una delle opzioni: ")
        go = txtIn.isdigit() and 5 > int(txtIn) > 0
    num = int(txtIn)
    match num:
        case 1:
            t.handleAdd(input("Inserisci una parola aliena e le traduzioni: ").lower())
        case 2:
            t.handleTranslate(input("Inserisci una parola da tradurre: ").lower())
        case 3:
            t.handleWildCard(input("Inserisci una parola da tradurre: ").lower())
        case 4:
            break
