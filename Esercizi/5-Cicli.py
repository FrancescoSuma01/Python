frutta = ['mela','pera', 'fragola']

#frutto è una varibile contatore
#in questo modo funziona solo con le liste
for frutto in frutta:
    print(frutto)

#stampa la stringa inserita lettera per lettera
for x in "banana":
    print(x)

#stampa i numeri da 0 a 9
for i in range(0, 10): #range crea una lisat al volo
    print(i)

#stampa l'elemento di frutta coincidente con il valore di i
for i in range(3):
    print(i, frutta[i])

#stampa il valore in elenco con al fianco numero di riga
elenco =  [12 , 23 , 34, 56]
i=0
for elemento in elenco:
    print('riga n. ', i , ': ', elemento)
    i += 1


#stampa i numeri con passo 2 i primi due valori sono il range l'ultimo è il passo
for i in range (0, 10, 2):
    print(i)



count = 0
while count < 5:
    print(count)
    count += 1


spesa = ['a', 'b']
i = 0

for elememto in spesa:
    print('(', i, ') ', elememto)
    i += 1