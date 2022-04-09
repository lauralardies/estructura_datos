# Imports necesarios para el ejercicio 1
from Ejercicio_1.mostrar import Mostrar
from Ejercicio_1.si import Si
from Ejercicio_1.bloque import Bloque
from Ejercicio_1.mientras_que import MientrasQue
from Ejercicio_1.visitante import Visitante

# Imports necesarios para el ejercicio 2
from Ejercicio_2.datos_usuario import DatosUsuario
from Ejercicio_2.mayusculas import Mayusculas
from Ejercicio_2.guardar import Guardar

# Imports necesarios para el ejercicio 3
from Ejercicio_3.naturaleza import Naturaleza
from Ejercicio_3.producto import Producto
from Ejercicio_3.factory_factura import FactoryFactura

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
linea1 = input("Por favor, introduzca la primera linea de su archivo: ")
linea2 = input("Por favor, introduzca la segunda linea de su archivo: ")
nombre_archivo = input("¿Cómo quiere llamar al archivo donde se va a guardar se texto?: ")
datos = DatosUsuario(linea1, linea2)
nuevos_datos = Mayusculas(datos).datos_procesados
Guardar(nombre_archivo, nuevos_datos)

# --- E J E R C I C I O  3 ---
producto = Producto(Naturaleza.ALIMENTARIA)
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
 
producto = Producto(Naturaleza.SERVICIO)
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 