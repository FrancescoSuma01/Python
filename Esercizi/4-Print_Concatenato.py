numeroA = 0
numeroB = 0
somma = 0

numeroA = input("Inserisci il primo valore: \n\r") #\n = nuova riga
numeroB = input("Inserisci il secondo valore: \n\r") #\r = ritorno a capo

somma = int(numeroA) + int(numeroB)

print(f"La somma tra {numeroA} e {numeroB} è: " , end =" ") #end = dopo aver scritto la stringa ci mette cio che è presente negli apici
print(somma)