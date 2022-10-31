class Calc:
    def __init__(self, operando1, operando2):
        self.operando1 = int(operando1)
        self.operando2 = int(operando2)
        self.risultato = 1

    def setOperazione(self, operazione):
        self.operazione = operazione

    def calcola(self):
        if (self.operazione == "+"):
            self.risultato = self.operando1 + self.operando2
        elif (self.operazione == "-"):
            self.risultato = self.operando1 - self.operando2
        elif (self.operazione == "x"):
            self.risultato = self.operando1 * self.operando2
        elif (self.operazione == "/"):
            self.risultato = self.operando1 / self.operando2
        print(self.risultato)
        

    def getRisultato(self):
        print(self.risultato)
        #return self.risultato

    def __str__(self):
        return f"{self.operando1} {self.operazione} {self.operando2} = "

def main():
    print("File non eseguibile")

if __name__ == "__main__":
    main()