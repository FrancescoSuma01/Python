from pycalclib import Calc
from sys import argv

def main():

    if not len(argv)==4:
        print("Paramtri non corretti")
    else:    
        c = Calc(argv[1],argv[3])
        c.setOperazione(argv[2])
        res = c.getRisultato()
        print(c, res)

if __name__=="__main__":
    main()