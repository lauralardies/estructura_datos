class Naturaleza():
    ALIMENTARIA = 5.5
    SERVICIO = 20

class Producto(Naturaleza):
    
    def __init__(self, iva) -> None:
        super().__init__()
        self.iva = iva
        self.producto = 100


class FactoryFactura():
    producto = None

    @classmethod
    def crear(cls, producto):
        cls.producto = producto

        return cls
    
    @classmethod
    def facturar(cls):
        return cls.producto.producto + (cls.producto.producto * cls.producto.iva / 100)

producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 105.5 
 
producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 120 