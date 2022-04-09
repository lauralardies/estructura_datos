# estructura_datos

Nuestra dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/estructura_datos)
https://github.com/lauralardies/estructura_datos

Para esta tarea había tres ejercicios distintos:
## Ejercicio 1:
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
## Ejercicio 2:

## Ejercicio 3:
