#Calcolatrice

def addizione(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    return a/b

print("Questa programma ti permette di eseguire calcoli tra due numeri")
n1 = int(input("Inserisci il primo valore: "))
n2 = int(input("Inserisci il secondo valore: "))
print ("Digita: \r")
print ("1) ADDIZIONE \r")
print ("2) SOTTRAZIONE \r")
print ("3) MOLTIPLICAZIONE \r")
print ("4) DIVISIONE \r")
operazione = int(input ("Digita ora il numero dell'operazione: \r\n"))
if (operazione == 1):
    somma = addizione(n1, n2)
    print(f"La somma dei valori {n1} e {n2} è : ", somma)
elif (operazione == 2):
    differenza = sottrazione(n1, n2)
    print(f"La differenza dei valori {n1} e {n2} è : ", differenza)
elif (operazione == 3):
    prodotto = moltiplicazione(n1, n2)
    print(f"Il prodotto dei valori {n1} e {n2} è : ", prodotto)
else:
    quoziente = divisione(n1, n2)
    print(f"Il quoziente dei valori {n1} e {n2} è : ", quoziente)
    