class Punto():
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y
    
    def impresion(self):
        return "el valor de x es= " + str(self.x) + " y el valor de y es = " + str(self.y)
  def opuesto(self):
    return Punto(-self.x, -self.y)

punto_a = Punto(9,12)
print(punto_a.impresion())

punto_b= opuesto.punto_a
print(punto_b.impresion())
    


    
    
  
