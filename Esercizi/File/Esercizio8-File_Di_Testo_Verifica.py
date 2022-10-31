import os

fname = input('nome file da cercare: ')

if os.path.exists(fname) :  #cerca il file con nome inserito da tastiera e restituisce un valore booleano
    print('trovato')
else :
    print('flie non trovato')
