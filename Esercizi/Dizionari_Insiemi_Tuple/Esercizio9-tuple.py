lista = [12, 23,34]   #lista(si puo modificare )

# tuple(non si puo modificare)
citta = ("milano", "roma", "napoli")
numeri_importanti = (3.14, 2.7, 1.1, 3.14)

print('-----------------intera-lista-un-elemnto-per-volta-------------')
for el in numeri_importanti :
    print(el)

#lettura singolo elemento di un tuple
print('-----------------singolo-elemento-----------------')
print(numeri_importanti[3])

#lunghezza o numeri di elemnti
print('-----------------numero-elementi-----------------')
n = len(numeri_importanti)
print('elemnti della tupla: ', n)

#fa una ricerca, nella lista o nella tupla, del valore inserito tra parentesi e stampa quante volte è presente
print('-----------------quante-volte-----------------')
n = numeri_importanti.count(3.14)
print(n)

#estrarre gli elementi con unwhile e con un indice
print('-----------------elenco-numerato-----------------')
i = 0
while (i < len(citta)) :
    print((i+1), citta[i])
    i += 1

#packing
valori = 3, 4.5, 'mela', 'euro'
print(valori)

#unpacking
a, b, c, d = valori
print(a)
print(b)
print(c)
print(d)

#ricerca di un elemento all'interno di una tupla
if "mela" in valori :
    print('trovato')
    pos = valori.index("mela") #mi da l'indice di mela all'interno della tupla
    print(pos)
else :
    print('non trovato')