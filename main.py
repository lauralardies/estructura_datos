from Ejercicio_1.mostrar import Mostrar
from Ejercicio_1.si import Si
from Ejercicio_1.bloque import Bloque
from Ejercicio_1.mientras_que import MientrasQue
from Ejercicio_1.visitante import Visitante

# --- E J E R C I C I O  1 ---
mostrar_ok = Mostrar('"OK"') 
mostrar_ko = Mostrar('"KO"') 
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
bloque_alternativa = Bloque() 
bloque_alternativa.agregarInstruction(alternativa) 
bucle = MientrasQue(True, bloque_alternativa) 

visitante = Visitante(bucle)
visitante.print_codigo()

# --- E J E R C I C I O  2 ---

# --- E J E R C I C I O  3 ---
