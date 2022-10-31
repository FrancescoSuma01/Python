"""
import random

segreto = random.randint(1,10)
risposta = 0
cont = 0

print ("Indovina il numero tra 1 e 10")
#print (segreto)
while risposta != segreto and cont < 5: #while not(risposta == segreto)
    risposta = int(input("Inserisci il numero: "))
    if risposta < segreto :
        print('Il numero da te inserito è minore dal numero segreto')
    elif risposta > segreto :
        print('Il numero da te inserito è maggiore del numero segreto')
    cont += 1

if cont < 5:
    print('Esatto')
else:
    print('Grazie di aver eseguito il programma. Ritenta sarai più fortunato')
"""

"""
count = 0
while count < 10 :
    print(count)
    count += 1
    if count == 5 :
        break #break = finisce il ciclo

print('end')

count = 0
while count < 10 :
    count += 1
    if count == 5 :
        print('xxx')
        continue #continue = salta il singolo passaggio e continua il ciclo
    print(count)
print('end')
"""

"""
num = [12, 23, 34, 45, 67, 78, 89]

for el in num :
    if el == 34:
        break
    print(el)

for el in num :
    if el == 34:
        continue
    print(el)

for el in num :
    if el%2 == 0:
        continue
    print(el)
"""

numeri = [12, 23, 34, 45, 56, 67, 78, 89, 90]
ripeti = True
while ripeti :
    trovato = False
    n=int(input('Che numero devo cercaere'))

    for el in numeri :
        if n == el :
            trovato = True
            break
    
    if trovato :
        print('il numero è stato trovato')
    else :
        print('il numero non è stato trovato')

    ans = input('vuoi eseguire nuovamente il progrmma? (si/no)')
    if ans != 'si' :
        ripeti = False

print('end')