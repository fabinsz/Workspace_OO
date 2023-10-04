from my_libraries.classes import Circulo, Retangulo, Triangulo, Quadrado

def workspace():
   f1 = Quadrado(4, 1, 2)
   print("Área do quadrado:", f1.CalcularArea())
   print("Perímetro do quadrado:", f1.CalcularPerimetro())
   print("Coordenadas do quadrado: x =", f1._x, "y =", f1._y)
   
   f2 = Retangulo(4, 6, 3, 5)
   print("Área do retangulo:", f2.CalcularArea())
   print("Perímetro do retangulo:", f2.CalcularPerimetro())
   print("Coordenadas do retangulo: x =", f2._x, "y =", f2._y)

   
if __name__ == "__main__":
    workspace()