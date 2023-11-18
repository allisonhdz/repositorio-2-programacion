#PRIMEROS CUATRO CODIGOS DE LA EVIDENCIA 2.1
#1
class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)


# bloque principal

persona1=Persona()
persona1.inicializar("Javier")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Perla")
persona2.imprimir()
