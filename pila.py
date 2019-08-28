class Pila:
    """define una clase Pila"""

    def __init__(self):
        """constructor de la clase"""
        self.items = []

    def esta_vacia(self):
        """indica si la pila está vacía"""
        
        if not self.items:
            return True
        return False
        
    def apilar(self,item):
        """apila un elemento al tope de la pila"""

        self.items.append(item)

    def desapilar(self):
        """desapila el último elemento agregado a la pila. Si está vacía, devuelve error"""
       
        if self.esta_vacia():
            raise IndexError('La pila está vacía')
        return self.items.pop()
