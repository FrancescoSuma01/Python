#Classe Genitore
class Auto:
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def setSpeed(self, speed):
        self.speed = speed

    def beep(self, sound):
        return f"Suono: {sound}"

    def __str__(self):
        return f"Auto: [{self.color}, {self.year}]"

#Classe Ereditaria
class Fiat500(Auto):
    def apriPortiera(self):
        print("portiera aperta")

    #Overwrite
    def __str__(self):
        return f"Fiat500: [{self.color}, {self.year}, {self.speed}]"

    #Overriding
    def beep(self, sound="bip bip"):
        return sound

#Classe Ereditaria
class Ferrari(Auto):
    def __str__(self):
        return f"Ferrari: [{self.color}, {self.year}, {self.speed}]"

    def beep(self, sound="Hoooohk"):
        return sound

print("-----Auto1-----")
a = Auto("rosso", 1995)
print (a)

print("-----Auto2-----")
b = Fiat500("blu", 2005)
b.setSpeed(40)
print(b.beep())
print(b)
b.apriPortiera()

print("-----Auto3-----")
c = Ferrari("Rossa", 1998)
print(c.beep())


print("-----Tipo di Oggetto-----")
#Ti dice se è o non è un oggetto di tipo auto
print(isinstance(a))