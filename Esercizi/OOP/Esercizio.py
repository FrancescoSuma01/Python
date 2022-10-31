class Auto:

    def __init__(self, cilindrata=5200, colore="rosso", trazione="posteriore", modello="BMW 520", velocità=315):
        self.cilindrata = cilindrata
        self.colore = colore
        self.trazione = trazione
        self.modello = modello
        self.velocità = velocità

    def verniciatura(self):
        self.colore = input("Di che colore vuoi verniciarela tua auto? ")

    def accellera(self):
        self.velocità = self.velocità + 10

    def __str__(self):
        return f"Auto: cilindarta {self.cilindrata}, colore {self.colore}, trazione {self.trazione}, modello {self.modello}, velocità {self.velocità}"    

car = Auto()

print(car) 