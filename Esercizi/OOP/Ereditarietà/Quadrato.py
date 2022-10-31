class Square:
    def __init__(self, l):
        self.l = l

    def area(self):
        return self.l * self.l

    def perimetro(self):
        return 4 * self.l

class Rect:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimetro(self):
        return 2*(self.l+self.w)

#Classe che eredita
class Square2(Rect):
    def __init__(self, l):
        #super prende il metodo dopo il punto dalla classe che lo eredita
        super().__init__(l, l)