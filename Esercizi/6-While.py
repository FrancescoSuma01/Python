import random   #libreria per generare numeri random

print ("* * * * *Conta fino a 10* * * * *\r")
count = 1 
while count <= 10:
    print (count)
    count += 1
print('fine conteggio \r')


print ("* * * * *Genera numeri casuali da 0 a 9 finche non è 7* * * * *\r")
n = 0
while not (n == 7):      #while (n != 7):
    n = random.randint(0,9)
    print(n)
print('fine conteggio \r')


print ("* * * * *Richiesta di uscita* * * * *\r")
risposta = 's'
while (risposta != 's'):
    risposta = input('Vuoi proseguire? s/n')
    print('.')
print('Ciao \r')
