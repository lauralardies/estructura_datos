class Bloque: 

    def __init__(self): 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
class Si: 
    
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
 
class MientrasQue: 
     
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 
 
class Mostrar: 
    
    def __init__(self, mensaje): 
        self.mensaje = mensaje 

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

mostrar_ok = Mostrar('"OK"') 
mostrar_ko = Mostrar('"KO"') 
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
bloque_alternativa = Bloque() 
bloque_alternativa.agregarInstruction(alternativa) 
bucle = MientrasQue(True, bloque_alternativa) 

visitante = Visitante(bucle)
visitante.print_codigo()