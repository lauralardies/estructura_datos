from Ejercicio_3.naturaleza import Naturaleza

class Producto(Naturaleza):
    
    def __init__(self, iva) -> None:
        super().__init__()
        self.iva = iva
        self.producto = 100