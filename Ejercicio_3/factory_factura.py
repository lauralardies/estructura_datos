class FactoryFactura():
    producto = None

    @classmethod
    def crear(cls, producto):
        cls.producto = producto

        return cls
    
    @classmethod
    def facturar(cls):
        return cls.producto.producto + (cls.producto.producto * cls.producto.iva / 100)