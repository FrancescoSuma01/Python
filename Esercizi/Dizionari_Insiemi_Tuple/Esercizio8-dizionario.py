listino = { #1: 2: 3: sono dette chiavi, "mela", "pera", "kiwi" sono detti valori
    1:"mela",
    2:"pera",
    3:"kiwi"
}
telefoni = {
    "mario rossi": 1234567890,
    "luigi bianchi": 3452344789,
    "pinco pallino": 9342063976
}

print (telefoni)

ntel = telefoni["pinco pallino"]
print (ntel)

k = listino.keys()                      #stampa l'elenco delle chiavi

v = listino.values()                    #stampa i valori

i = listino.items()                     #stampa tutto il dizionario a coppie

if "pinco pallino" in telefoni :        #verifica se è presente un elemento
    print ('presente')

telefoni['tizio caio'] = 3457892873     #aggiunge questo elemento al dizionario

telefoni["tizio caio"] = 5393672390     #modifica il valore della chiave

telefoni.pop["tizio caio"]              #elimina 'tizio caio' dal dizionario

telefoni.clear()                        #elimina tutto

cell = telefoni.copy()                  #fa una copia di telefoni
cell2 = dict(telefoni)                  #fa una copia di telefoni 