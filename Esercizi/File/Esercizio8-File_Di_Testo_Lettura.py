fileditesto = open("prova.txt")   #cerca il file e lo apre
print(fileditesto.read())         #legge il contenuto del file e lo stampa
print("---------------------------------\n")
fileditesto.seek(0)               #torna all'inizio del file 
token = fileditesto.read(1)         #stampa il numero di caratteri presenti nella parentesi
print(token)
print("---------------------------------\n")
fileditesto.seek(0)               #torna all'inizio del file fileditesto.seek(0) 
linea = fileditesto.readline()    #stampa un intera linea a partire da dove sta seek
print (linea)
print("---------------------------------\n")
fileditesto.seek(0)               #torna all'inizio del file fileditesto.seek(0)
i = 1
for ln in fileditesto :           #stampa tutto il contenuto
    print(i, ln)
    i += 1