class Shape():
    def __init__(self, l, w):
        self.l = l
        self.w = w

class Coloured():
    def __init__(self, color):
        self.color = color

class Rect(Shape):
    def __init__(self, l, w):
        super.__init__(l, w)

    def area(self):
        return self.l * self.w

    def perimetro(self):
        return 2*(self.l+self.w)

class Square(Rect, Coloured):
    def __init__(self, l, color):
        Rect.__init__(self, l, l)
        Coloured.__init__(self, color)
     

r = Rect(2, 3)
print(f"Area: {r.area}")
q = Square(4, "Rosso")
print(f"Area: {q.area}")