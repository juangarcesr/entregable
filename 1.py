#se crea el repositorio

class Implante():
    def __init__(self, material, tamaño,estado,frevision,fmantenimiento):
        self.__material = material
        self.__tamaño = tamaño
        self.__estado=estado
        self.__frevision= frevision
        self.__fmantenimiento= fmantenimiento
  
    def verMaterial(self):
       return self.__material
    def verTamaño(self):
       return self.__tamaño
    def verEstado(self):
       return self.__estado
    def verfmantenimiento(self):
       return self.__fmantenimiento
    def verfrevision(self):
       return self.__frevision
  
    def asignarTamaño(self,ta):
       self.__tamaño=ta
    def asignarMaterial(self,m):
       self.__material=m
    def asignarEstado(self,e):
       self.__estado=e
    def asignarFmantenimiento(self,fmantenimiento):
       self.__fmantenimiento = fmantenimiento
    def asignarFrevision(self,frevision):
       self.__frevision = frevision

    def __str__(self):
       return f'El estado del implante es{self.verEstado} \n Tamaño: {self.verTamaño} \n Material: {self.verMaterial} \n Fecha de mantenimiento: {self.verfmantenimiento}\n Fecha de revisión: {self.verfrevision}'
    
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
  
  def __init__(self,material,fijacion,forma,estado,tamaño):
    super().__init__(material,estado,tamaño)   
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
  def __init__(self,NumElectrodos,frecuenciasEstimulacion,estado,tamaño,material):
    super().__init__(estado,tamaño,material)
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

class ProtesisRodilla(Implante):
  def __init__(self,material,fijacion,tamaño,estado):
    super().__init__(material,tamaño,estado)
    self.__Fijación = fijacion

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación

class Sistema(Implante):
  def __init__(self, material, tamaño,estado,frevision,fmantenimiento):
        super().__init__(estado,tamaño,material,frevision, fmantenimiento)
        self.__inventario = []

  def agregar_implante(self, implante):
        self.__inventario.append(implante)
        return True
  
  def seguimientoImplante (self,frevision,fmantenimiento):
     self.__frevision = Implante.verfmantenimiento
     self.__fmantenimiento = Implante.verfrevision
     return self.__frevision
     return self.__fmantenimiento
  
  def editar(self,implante,material, tamaño,estado,frevision,fmantenimiento):
     self.__material = Implante.asignarMaterial
     self.__tamaño = Implante.asignarTamaño
     self.__estado = Implante.asignarEstado
     self.__frevision = Implante.asignarFrevision
     self.__fmantenimiento = Implante.asignarFmantenimiento

  def eliminar_implante(self, implante):
        self.inventario.remove(implante)
  
  def verNumeroImplantes(self):
        print("En el sistema hay: " + str(len(self.__inventario)) + " implantes")
  
  def visualizar_inventario(self):
        for implante in self.inventario:
            print(implante) 

  def verificarExiste(self,c):
        return c in self.__inventario
  def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("Ingrese un dato numérico...")
    return valor

class Paciente():
  
  def __init__(self,id,implante,medico,fimplantacion, estadoimplante):
     self.__id = id
     self.__implante = implante
     self.__medico = medico
     self.__fimplantacion = fimplantacion
     self.__estadoimplante = estadoimplante
  
  def verID (self):
    return self.__id
  def verImplante (self):
    return self.__implante
  def verMedico(self):
    return self.__medico
  def verFimplantacion (self):
    return self.__fimplantacion
  def verEstadoImplante (self):
    return self.__estadoimplante

  def asignarID (self,id):
    self.__asignarID = id
  def asignarImplante (self,implante):
    self.__asignarImplante = implante
  def asignarMedico(self, medico):
    self.__asignarMEdico =medico
  def asignarFimplantacion (self,fimplantacion):
    self.__asignarFimplantacion = fimplantacion
  def asignarEstadoImplantación (self,estadoImplantacion):
    self.__asignarEstado = estadoImplantacion

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
            tipo_implante = input("""Ingrese el tipo de implante que desea ingresar:
            1. protesis de cadera
            2. stent coronario
            3. implante dental
            4. marcapasos
            5. protesis de rodilla
            > """)
            #tipo = input("Ingrese el tipo de implante: ")
            material = input("Ingrese el material del implante: ")
            tamaño = input("Ingrese el tamaño del implante: ")
            estado = input("Ingrese el estado del implante: ")
            
            if tipo_implante == "1":
                fijacion = input("Ingrese el tipo de fijación de la prótesis de cadera: ")
                implante = ProtesisCadera( material, tamaño, estado, fijacion)
            elif tipo_implante == "2":
                longitud = input("Ingrese la longitud del stent coronario: ")
                diametro = input("Ingrese el diámetro del stent coronario: ")
                implante = StentCoronario( material,tamaño, longitud, diametro, estado)
            elif tipo_implante == "3":
                forma = input("Ingrese la forma del implante dental: ")
                fijacion = input("Ingrese el tipo de fijación del implante dental: ")
                implante = ImplanteDental( material, tamaño, estado, forma, fijacion)
            elif tipo_implante == "4":
                num_electrodos = input("Ingrese el número de electrodos del marcapasos: ")
                frecuencia_estimulacion = input("Ingrese la frecuencia de estimulación del marcapasos: ")
                implante = Marcapasos( material, tamaño, estado, num_electrodos, frecuencia_estimulacion)
            elif tipo_implante == "5":
                fijacion = input("Ingrese el tipo de fijación de la prótesis de rodilla: ")
                implante = ProtesisRodilla( material, tamaño, estado, fijacion)
            
            base.agregar_implante(implante)
        elif menu =="2":
            implante = input("Implante a eliminar: ")
            print(base.eliminar_implante)
            
        elif menu =="3":
           implante = input("Implante: ")
           print(Implante.__str__)

        elif menu == "4":
           editar=input("Implante a editar:")
           if editar == tipo_implante:
              Sistema.editar

        elif menu =="5":
            break
        else:
            print("Salió del sistema.")
            break

if __name__ == '__main__':
    main()
