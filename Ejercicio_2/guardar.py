class Guardar():

    def __init__(self, nombre_archivo, nuevos_datos) -> None:
        self.texto_archivo = nuevos_datos
        self.nombre_archivo = nombre_archivo
        f = open(self.nombre_archivo + ".txt", "w", encoding="utf8")
        f.write(self.texto_archivo.l1 + "\n" + self.texto_archivo.l2)
        f.close