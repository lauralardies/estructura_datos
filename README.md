# estructura_datos

Nuestra dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/estructura_datos)
https://github.com/lauralardies/estructura_datos

Para esta tarea había tres ejercicios distintos:
## Ejercicio 1
Este ejercicio consiste en crear una clase que recorra una serie de clases. El objetivo de esta nueva clase (llamada visitante) es que sea capaz de imprimir este mismo mensaje:
```
while True: 
   if 2 + 2 == 4: 
          print("OK") 
   else: 
          print("KO")
```
La clase que he desarrollado para que muestre el mensaje anterior es la siguiente:
```
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
```
En el código principal llamamos sólo a la última función, pues esta ejecuta las dos anteriores:
```
visitante = Visitante(bucle)
visitante.print_codigo()
```
## Ejercicio 2
El ejercicio 2 trata de pedirle al usuario dos líneas de texto. Seguidamente, el código cambia estas dos líneas de texto a mayúsculas y las introduce en un archivo txt, cuyo nombre es elegido por el usuario. La importancia de este ejercicio es centrarse en realizar un código siguiendo la filosofía MVC. Para ello, he creado tres clases: 
- Clase 1.
```
class DatosUsuario:

    def __init__(self, linea1, linea2) -> None:
        self.l1 = linea1
        self.l2 = linea2
```
- Clase 2.
```
class Mayusculas():

    def __init__(self, datos) -> None:
        self.datos_procesados = DatosUsuario
        self.datos_procesados.l1 = datos.l1.upper()
        self.datos_procesados.l2 = datos.l2.upper()
```
- Clase 3.
```
class Guardar():

    def __init__(self, nombre_archivo, nuevos_datos) -> None:
        self.texto_archivo = nuevos_datos
        self.nombre_archivo = nombre_archivo
        f = open(self.nombre_archivo + ".txt", "w", encoding="utf8")
        f.write(self.texto_archivo.l1 + "\n" + self.texto_archivo.l2)
        f.close
```
El código principal que ejecuta las clases que acabamos de nombrar es el siguiente:
```
linea1 = input("Por favor, introduzca la primera linea de su archivo: ")
linea2 = input("Por favor, introduzca la segunda linea de su archivo: ")
nombre_archivo = input("¿Cómo quiere llamar al archivo donde se va a guardar se texto?: ")
datos = DatosUsuario(linea1, linea2)
nuevos_datos = Mayusculas(datos).datos_procesados
Guardar(nombre_archivo, nuevos_datos)
```
## Ejercicio 3
