#definizione della classe(Nome della classe iniziale maiuscola)
class Led:
  
    #metodi
    #init-->costruttore
    def __init__(self, colore, stato):
        #
        self.colore = colore
        self.stato = stato
    
    def accendi(self):
        self.stato = "on"

    def spegni(self):
        self.stato = "off"

    def setTensione(self, volt):
        self.tensione = volt
    
    def getTensione(self):
        return self.tensione

    def setStato(self, stato):
        self.stato = stato

    def getStato(self):
        return self.stato

    def getColore(self):
        return self.colore
        
    #non buono
    #def toString(self):
        #return (f"colore: {self.colore}, stato: {self.stato}, tensione: {self.tensione}")

    def __str__(self):
        return (f"colore: {self.colore}, stato: {self.stato}, tensione: {self.tensione}")


mioled = Led("rosso", "off")

print("colore mioled: ", mioled.colore)
print("stato mioled: ", mioled.stato)

mioled.accendi()
print("stato mioled dopo accendi: ", mioled.stato)

mioled.spegni()
print("stato mioled dopo accendi: ", mioled.stato)

mioled.setTensione(12)
print("Tensione mioled: ", mioled.tensione)

print(mioled)