class ValorDePi():
    Pi = 3,14

class formas_geometricas():
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def updateCoord(self,x,y):
        self._x= x
        self._y= y

    def CalcularArea(self):
        pass

    def CalcularPerimetro(self):
        pass

class Quadrado(formas_geometricas):
    def __init__(self, x, y, lado):
        super().__init__(x, y)
        self.lado = lado

    def updateCoord(self,x,y):
        super().updateCoord(x, y)

    def CalcularArea(self):
        return self.lado ** 2

    def CalcularPerimetro(self):
        return 4 * self.lado

class Retangulo(formas_geometricas):
    def __init__(self, x, y, base, altura):
        super().__init__(x, y)
        self.base = base
        self.altura = altura
    def updateCoord(self,x,y):
        super().updateCoord(x, y)

    def CalcularArea(self):
        return self.base * self.altura    
    
    def CalcularPerimetro(self):
        return 2 * (self.base + self.altura)
    
class Triangulo(formas_geometricas):
    def __init__(self, x, y, base, altura):
        super().__init__(x, y)   
        self.base = base
        self.altura = altura
     
    def updateCoord(self,x,y):
        super().updateCoord(x, y) 

    def CalcularArea(self):
        return (self.base * self.altura) / 2

    def CalcularPerimetro(self):
        return self.base + 2 * ((self.base**2 + self.altura**2)**0.5)

class Circulo(formas_geometricas, ValorDePi):  
    def __init__(self, x, y, raio):
        super().__init__(x, y)   
        self.raio = raio
    
    def updateCoord(self,x,y):
        super().updateCoord(x, y)

    def CalcularArea(self):
        return ValorDePi.Pi * (self.raio**2)
    
    def CalcularPerimetro(self):
        return ValorDePi.Pi * 2 * self.raio
           