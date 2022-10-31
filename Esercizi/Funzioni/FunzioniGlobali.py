a = 10

#questa funzione non modifica la variabile a
def f1(a):
    a = 20
    print("nella funzione a= ", a)

#questa funzione modifica la variabile a
def f_che_modifica(n):
    a = n*2
    return a

#non buono da usare
def f3():
    #cerca esternamente alla funzione, trova la variabile e la modifica
    global a
    a = 30
    print("nella funzione a= ", a)

print(a)
f1()
print("dopo la chiamata di f1 a= ",a)

a = f_che_modifica(a)
print("dopo la chiamata di f_che_modifica a= ",a)

f3()
print("dopo la chiamata di f3 a= ",a)