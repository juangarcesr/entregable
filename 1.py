#se crea el repositorio


class Implante():
    def __init__(self, tipo, material, tamaño,estado):
        self.__tipo = tipo
        self.__material = material
        self.__tamaño = tamaño
        self.__estado=estado
    def verTipo(self):
       return self.__tipo
    def verMaterial(self):
       return self.__material
    def verTamaño(self):
       return self.__tamaño
    def verEstado(self):
       return self.__estado
    
    def asignarTipo(self,t):
       self.__tipo=t
    def asignarTamaño(self,ta):
       self.__tamaño=ta
    def asignarMaterial(self,m):
       self.__material=m
    def asignarEstado(self,e):
       self.__estado=e


    #def __str__(self): (NO SÉ SI SEA NECESARIO ESTE STR)
      #  return f'el tipo de implante es: {self.verTipotipo}, el material es {self.verMaterialmaterial}, Tamaño: {self.verMaterialtamaño}'   
    def __str__(self):
       return f'el estado del implante es{self.verEstado}'

class ProtesisCadera(Implante):
  def __init__(self,material,fijacion,tamaño,estado):
    super().__init__(material,tamaño,estado)
    self.__Fijación = fijacion

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación

class StentCoronario(Implante):
  def __init__(self,material,longitud,diametro,tamaño,estado):
     super().__init__(material,tamaño,estado)
     self.__Longitud = longitud
     self.__Diametro = diametro      

  def verLongitud (self):
    return self.__Longitud
  def asignarLongitud (self, Longitud):
    self.__Longitud = Longitud

  def verDiametro (self):
    return self.__Diametro
  def asignarDiametro (self, Diametro):
    self.__Diametro = Diametro

class ImplanteDental(Implante):
  
  def __init__(self,material,fijacion,forma,estado):
    super().__init__(material,estado)   
    self.__Fijación = fijacion
    self.__forma=forma

  def verForma (self):
    return self.__forma
  def asignarForma (self, Fo):
    self.__forma=Fo 

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación

class Marcapasos(Implante):
  def __init__(self,NumElectrodos,tipo,frecuenciasEstimulacion,estado):
    super().__init__(tipo,estado)
    self.__NumeroElectrodos = NumElectrodos
    self.__FrecuenciaEstimulacion = frecuenciasEstimulacion

  def verNumElectrodos (self):
    return self.__NumeroElectrodos
  def asignarNumElectrodos (self, n):
    self.__NumeroElectrodos = n

  def verFrecuenciaEstimulacion(self):
    return self.__FrecuenciaEstimulacion
  def asignarFrecuenciaEstimulacion(self, e):
    self.__FrecuenciaEstimulacion = e

class ProtesisRodilla():
  def __init__(self,material,fijacion,tamaño,estado):
    super().__init__(material,tamaño,estado)
    self.__Fijación = fijacion

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación
class Sistema():
  
  def __init__(self):
        self.__inventario = []

  def agregar_implante(self, implante):
        self.__inventario.append(implante)
        return True
  
  def eliminar_implante(self, implante):
        self.inventario.remove(implante)
  
  def verNumeroImplantes(self):
        print("En el sistema hay: " + str(len(self.__inventario)) + " implantes")
  
  def visualizar_inventario(self):
        for implante in self.inventario:
            print(implante) 

  def verificarExiste(self,c):
        return c in self.__inventario

def main():
    base = Sistema()
    while True:
        menu = input("""Seleccione una opción:
        1. Ingresar un nuevo implante.
        2. Eliminar un implante.
        3. Selección de implante.
        4. Editar datos de implante.
        5. Salir.
        > """)
        if menu == "1": 
            pass 
            b = Implante()
            b.asignarTipo=input("ingrese el tipo de implante")
            b.asignarTamaño = input("ingrese el tamaño del implante: ")
            b.asignarEstado = input("ingrese el estado del implante: ")
            b.asignarMaterial= input("ingrese el material del que está hecho el implante:  ")
            

            tipo_implante = input("""Ingrese el tipo de implante que desea ingresar:
            1. protesis de cadera
            2. stent coronario
            3. implante dental
            4. marcapasos
            5.protesis de rodilla 
                                                                            
            > """)
            if tipo_implante == "1":
                v=ProtesisCadera
                v.asignarFijacion = input("ingrese el tipo de fijacion del implante: ")

            elif tipo_implante == "2":
                r=StentCoronario
                r.asignarLongitud = input("ingrese la longitud del stent: ")
                r.asignarDiametro=input("ingrese el diametro del stent: ")

            elif tipo_implante == "3":
                j=ImplanteDental
                j.asignarForma = input("ingrese la forma del implante: ")
                j.asignarFijacion=input("ingrese el tipo de fijacion del implante:")
            
            elif tipo_implante == "4":
                t=Marcapasos
                t.asignarFrecuenciaEstimulacion = input("ingrese la frecuencia de estimulación del marcapasos:  ")
                t.asignarNumElectrodos=input("ingrese el numero de electrodos: ")

            elif tipo_implante == "5":
                q=ProtesisRodilla
                q.asignarFijacion = input("ingrese la forma de fijación: ")

            base.agregar_implante(b)
        elif menu =="2" :
            pass
        elif menu =="3":
           pass

        elif menu =="5":
            break
        else:
            print("salió del sistema.")
            break

if __name__ == '__main__':
    main()


