from math import cos
from math import sin
from math import radians

ARRIBA = False
ABAJO = True

class Pluma:
    """Clase que define los distintos estados del objetos Pluma"""

    def __init__(self,color = 'black',ancho = 10 ,estado = ABAJO):
        """constructor de la clase"""
        
        self.color = color
        self.ancho = ancho
        self.estado = estado
    
    def __str__(self):
        """devuelve un str del estado de la pluma: True o False"""

        return f'{self.estado}'

    def cambiar_estado(self):
        """Habilita o desabilita el uso de la pluma"""

        self.estado = not(self.estado)

class Tortuga:
    """Clase que define los distintos estados del objeto Tortuga"""

    def __init__(self, pluma, x = 0, y = 0, orientacion = 0):
        """Constructor de la clase"""
        
        self.posicion = [x,y]
        self.pluma = pluma
        self.orientacion = orientacion

    def adelante(self,n):
        """Adelanta n avance la posición de la tortuga en el mapa"""

        self.posicion[0] += float(cos(self.orientacion) * n)
        self.posicion[1] += float(sin(self.orientacion) * n)

    def derecha(self,angulo):
        """Cambia la orientación de la tortuga girando hacia la derecha los ángulos pasados por parámetro"""

        self.orientacion -= angulo
    
    def izquierda(self,angulo):
        """Cambia la orientacion de la tortuga girando hacia la izquierda los ángulos pasados por parámetro"""

        self.orientacion += angulo
