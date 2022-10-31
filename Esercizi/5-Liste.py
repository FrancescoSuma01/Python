eta = [12, 16, 4, 45, 44]
nomi = ['Topolino', 'Pippo', 'Paperino', 'Minnie', 'Pluto']
misto = [10, 25.4, -10, 'Roma']

#stampa un nome per riga
print ("* * * * *STAMPA NOMI RIGA PER RIGA* * * * *")
print(nomi[0])
print(nomi[1])
print(nomi[2])
print(nomi[3])
print(nomi[4]) 

#stampa tutta la lisat come è stata dichiarata
print ("* * * * *STAMPA NOMI SULLA STESSA RIGA* * * * *")
print(nomi)

#stampa la lunghezza della lista
print ("* * * * *LUNGHEZZA DELLA LISTA NOMI* * * * *")
print("La lunghezza della lista nomi è: ", len(nomi))

#aggiunge cio che è presente nelle parentesi alla fine della lista inserita prima del punto
print ("* * * * *AGGIUNTA DI UN ELEMENTO* * * * *")
nomi.append('Ciao')
print(nomi)

#aggiunge Ciao nella posizione 1
nomi.insert(1, 'Ciao')

#toglie l'elemento indicato
print ("* * * * *TOGLIE UN ELEMENTO INDICATO* * * * *")
nomi.remove('Ciao')
print(nomi)

#toglie l'elemento alla posizione
print ("* * * * *TOGLIE UN ELEMENTO SAPENDO LA POSIZIONE* * * * *")
nomi.pop(4)
print(nomi)

#inserisce più elementi alla lista
print ("* * * * *INSERISCE PIù ELEMENTI ALLA LISTA* * * * *")
nomi.insert(5, 'Hello')
print(nomi)

#Stampa la posizione dell'elemento tra parentesi
print(nomi.index("Pluto"))

#elimina l'ultimo elemento di una lista
print ("* * * * *ELIMINA L'ULTIMO ELEMENTO ALLA LISTA* * * * *")
nomi.pop()
print (nomi)

#stampa gli elemnti della lista compresi tra il primo valore e il secondo, quindi in questo caso 1;2;3;4
print ("* * * * *STAMPA GLI ELEMENTI DELLA LISTA IN UN DETERMINATO RANGE* * * * *")
print (nomi[1:5])

#ordina la lista eta
eta.sort()
print (eta)

print ("* * * * *STAMPA UNA MATRICE* * * * *")
matrice = int[ [1, 2, 3], [4, 5, 6] ]
print (matrice)