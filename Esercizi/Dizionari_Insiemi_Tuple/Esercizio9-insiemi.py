#insiemi
s = {'a', 'b', 'c'}      #se ci sono du elemnti uguali ne stampa uno solo
a = {11, 22, 33, 44, 55, 66, 77, 88}
set1 = set([])           #insieme vuoto

print("-----------------tutto-l'insieme-----------------")
print(a)
print("-----------------con-il-99----------------")
a.add(99)             #aggiunge l'emento tra parentesi all'insieme
print(a)

print("-----------------senza-il-99----------------")
a.discard(99)         #elimina il numero 99
print(a)

print("-----------------svuota-l'insieme-----------------")
a.clear()             #svuota l'insieme
print(a)

print("-----------------unione------------------")
A = {1, 3, 5, 7, 9}      #insieme A
B = {2, 4, 6, 8, 10}     #insieme B
C = A.union(B)           #insieme C = insieme A + insieme B
print (C)

print("-----------------intersezione------------------")
D = A.intersection(B)    #insieme C = numeri in comune tra insieme A einsieme B
print (D)

print("-----------------differenza------------------")
E = A.difference(B)      #stampa i numeri che non sono presenti in tutte e due le liste prendendo in campioneunasola lista
print(E)

G = A.symmetric_difference(B)   #parti non comuni ai due
print (G)

print("-----------------verifica-presenza-elemento----------------")
if 5 in A :
    print('è presente')
else :
    print('non è presente')

print("------------------scorro-l'insieme----------------")
for el in A :
    print(el)