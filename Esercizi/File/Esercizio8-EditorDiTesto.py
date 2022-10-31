import os
testo = []
line = ""

print("Inserisci 'quit' per uscire dal programma")
while True :
    line = input("> ")
    if (line == 'quit') :
        break
    elif (line == "!"):
        i = 1
        for el in testo :
            print(f"{i} : {el}")
            i += 1
    elif (line == 'r') :
        n = input('che riga vuoi cancellare: ')
    elif (line == 'f') :
        n = input('che parola vuoi cercare? ')
    elif (line == 'l') :
        n = input('che file vuoi aprire? ')
        if os.path.exists(n) :
            #posso leggere il file 
            testo = []
            f = open(n)
            for riga in f :
                testo.append(riga)
        else : 
            print('il file non esiste')
    elif (line == 's') :
        n = input("dammi il nome del file: ")
        f = open(n, "x")
        for riga in testo :
            f.write(riga+"\n")
        f.close()
    else :
        testo.append(line)