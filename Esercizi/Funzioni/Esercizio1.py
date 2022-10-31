#funzioni

"""def saluta():     #definizione della funzione
    print ("ciaoo")

saluta()"""

def saluta(nome):     #definizione della funzione
    print ("ciaoo", nome)

def somma1(a, b):    #a e b sono paramtri
    somma = a + b
    return somma

def prod(a, b):    #a e b sono paramtri
    return a*b

def cugini(*kids):  #questa funzione non sa quanti parametri riceverà
    n = len(kids)
    print ("numero di argomenti: ", n)
    print (kids[2])

def impostaSerra(temp, hum, luce):
    print("Temperatura = ", temp)
    print("Umidità = ", hum)
    print("Luce = ", luce)

def paeseNascita(nazione = "Svizzera"):
    print ("spedire in ", nazione)

def printLista(lista):
    c = 1
    for x in lista:
        print (c, x)
    c += 1

def esempio():
    pass    #se ancora non so cosa devo mettere in questa funzione metto pass e salta la funzione    

def multiop(a, b):
    somma = a + b
    prodotto = a * b
    return somma, prodotto

n = somma1(10, 12)   #10 e 12 sono argomenti
print ("La somma dei numeri inseriti è: ",n)

print("-----------------------------------------------")

n = prod(2, 10)
print ("Il prodotto dei valori inseriti è: ",n)

print("-----------------------------------------------")

saluta("Francesco")

print("-----------------------------------------------")

#cugini("Aldo")
#cugini("Aldo", "Giovanni")
cugini("Aldo", "Giovanni", "Giacomo")

print("-----------------------------------------------")

impostaSerra(24, 50, 99) #se ti ricordi l'ordine con cui hai dichiarato i parametri
impostaSerra(hum = 50, luce = 99, temp = 24) #se NON ti ricordi l'ordine con cui hai dichiarato i parametri

print("-----------------------------------------------")

paeseNascita("svizzera")   #paeseNascita è uguale a svizzera se non metto nulla ma lo metto come parametro fa la stessa cosa
print("-----------------------------------------------")

frutta = ["mela", "pera", "banana"]
printLista(frutta)

print("-----------------------------------------------")

n = multiop(3,2)
print(n)         #cosi mi stampa una tupla con somma al primo posto e il profìdotto al secondo posto in questo caso
somma, prodotto = multiop(3,2)   #assegna in automati il primo valore a somma e il secondo al prodotto
print (somma)
print (prodotto) 