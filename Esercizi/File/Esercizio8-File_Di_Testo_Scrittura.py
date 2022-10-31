#f = open("prova.txt", 'w') #apre il file per scrivere ma all'apertura del file elimina il contanuto
f = open("prova.txt", 'a') #apre il file in scrittura ma con la modalità append(aggiungi) quindi non elimina nulla

f.write("mele \n")
f.write("pere \n")
f.write("fragole \n")
f.close()