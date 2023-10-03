from my_libraries.classes import Circulo, Retangulo, Triangulo, Quadrado

def workspace():
   f1 = Quadrado(4, 1, 2)
   print("Área do quadrado:", f1.CalcularArea())
   print("Perímetro do quadrado:", f1.CalcularPerimetro())
   print("Posição do quadrado:", f1.updateCoord())
   
   f2 = Retangulo(4, 6, 3, 5)
   print("Área do retangulo:", f2.CalcularArea())
   print("Perímetro do retangulo:", f2.CalcularPerimetro())
   print("Posição do retangulo:", f2.updateCoord())

   
if __name__ == "__main__":
    workspace()