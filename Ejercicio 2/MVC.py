class DatosUsuario:

    def __init__(self, linea1, linea2) -> None:
        self.l1 = linea1
        self.l2 = linea2

class Mayusculas():

    def __init__(self, datos) -> None:
        self.datos_procesados = DatosUsuario
        self.datos_procesados.l1 = datos.l1.upper()
        self.datos_procesados.l2 = datos.l2.upper()
 

class Guardar():

    def __init__(self, nombre_archivo, nuevos_datos) -> None:
        self.texto_archivo = nuevos_datos
        self.nombre_archivo = nombre_archivo
        f = open(self.nombre_archivo + ".txt", "w", encoding="utf8")
        f.write(self.texto_archivo.l1 + "\n" + self.texto_archivo.l2)
        f.close

linea1 = input("Por favor, introduzca la primera linea de su archivo: ")
linea2 = input("Por favor, introduzca la segunda linea de su archivo: ")
nombre_archivo = input("¿Cómo quiere llamar al archivo donde se va a guardar se texto?: ")
datos = DatosUsuario(linea1, linea2)
nuevos_datos = Mayusculas(datos).datos_procesados
Guardar(nombre_archivo, nuevos_datos)