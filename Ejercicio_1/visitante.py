from Ejercicio_1.si import Si

class Visitante:
    def __init__(self, bucle) -> None:
        self.bucle = bucle
     
    def print_while(self):
        print("while " + str(self.bucle.condicion) + ":")

    def print_bloque(self):
        for i in range(0, len(self.bucle.bloque.instrucciones)):
            if isinstance(self.bucle.bloque.instrucciones[i], Si):
                print("\tif " + str(self.bucle.bloque.instrucciones[i].condicion) + ":")
                print("\t\tprint(" + str(self.bucle.bloque.instrucciones[i].entonces.mensaje) + ")")
                print("\telse:")
                print("\t\tprint(" + str(self.bucle.bloque.instrucciones[i].si_no.mensaje) + ")")
        
    def print_codigo(self):
        self.print_while()
        self.print_bloque()