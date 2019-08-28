class Cola:
    """define una clase Cola"""

    def __init__(self):
        """constructor de la clase"""
        self.items = []
    
    def encolar(self,item):
        """agrega elementos al final de la cola"""
        self.items.append(item)
    
    def desencolar(self):
        """quita el primer elemento de la cola. Si está vacía, devuelve error"""

        if self.esta_vacia():
            raise ValueError('La cola está vacía')
        return self.items.pop(0)
    
    def esta_vacia(self):
        """indica si la cola está vacía"""

        if not self.items:
            return True
        return False

    
