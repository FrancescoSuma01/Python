#as ml fa si che per chiamare miaLibreria basta semplicemente mettere ml
#import prende tutta la libreria
import miaLibreria as ml
#from prende solo la funzione che sta dopo import(consigliato)
from miaLibreria import somma
#importa prod e cambia il nome con nul
from miaLibreria import prod as nul

__name__

def main():
    print("ciao mondo")
    ml.hello()

    n = somma(10, 20)
    print(n)

    n = nul(10, 30)
    print(n)

if __name__ == "__main__":
    main()