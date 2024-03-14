#se crea el repositorio

import datetime
class Implante():
    def __init__(self, material, tamaño,estado):
        #self.__tipo = tipo
        self.__material = material
        self.__tamaño = tamaño
        self.__estado=estado
   # def verTipo(self):
     #  return self.__tipo
    def verMaterial(self):
       return self.__material
    def verTamaño(self):
       return self.__tamaño
    def verEstado(self):
       return self.__estado
    
   # def asignarTipo(self,t):
    #   self.__tipo=t
    def asignarTamaño(self,ta):
       self.__tamaño=ta
    def asignarMaterial(self,m):
       self.__material=m
    def asignarEstado(self,e):
       self.__estado=e


    #def __str__(self): (NO SÉ SI SEA NECESARIO ESTE STR)
      #  return f'el tipo de implante es: {self.verTipotipo}, el material es {self.verMaterialmaterial}, Tamaño: {self.verMaterialtamaño}'   
    def __str__(self):
       return f"Tipo: {self.verEstado}\nMaterial: {self.verMaterial}\nTamaño: {self.verTamaño}"
    
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

class Paciente():
   def __init__(self,nombre,cedula):
      self.__nombre=nombre
      self.__cedula=cedula
      self.__Protesis= []

   def verProtesis(self):
      return self.__Protesis 
   def agregarProtesis(self, protesis, fecha_implantacion, medico_responsable, estado):
        self.__protesis.append({
            'protesis': protesis,
            'fecha_implantacion': fecha_implantacion,
            'medico_responsable': medico_responsable,
            'estado': estado
        }) 
   def verMombre (self):
    return self.__nombre
   def verCedula(self):
      return self.__cedula
   def verProtesis(self):
      return self.__protesis
   
   #def agregarProtesis(self, tipo_implante, protesis):
    #  self.__protesis[tipo_implante] = protesis
   def asignarNombre(self,n):
      self.__nombre=n
   def asignarCedula(self,c):
      self.__cedula=c

class Sistema():
  
  def __init__(self):
        self.__inventario = []
        self.__pacientes=[]

  def agregar_implante(self, implante):
        self.__inventario.append(implante)
        return True
  
  def eliminar_implante(self, implante):
        if implante in self.__inventario:
            self.__inventario.remove(implante)
            print("Se eliminó el implante")
        else:
            print("no existe el implante")

  def asignar_implante_a_paciente(self, cedula_paciente, tipo_implante, fecha_implantacion, medico_responsable, estado):
        paciente_encontrado = False
        for paciente in self.__pacientes:
            if paciente.verCedula() == cedula_paciente:
                for implante in self.__inventario:
                    if isinstance(implante, tipo_implante):
                        paciente.agregarProtesis(implante, fecha_implantacion, medico_responsable, estado)
                        paciente_encontrado = True
                        print("Implante asignado al paciente correctamente.")
                        break
                break
        if not paciente_encontrado:
            print("No se encontró al paciente o no hay implantes disponibles del tipo seleccionado.")
  
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
        3. Asingar una protesis a un paciente            
        4. Verificar exixtencia de implante
        5. visualizar inventario.
        6. Salir.
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
            pass
        elif menu =="3":

          cedula_paciente = input("Ingrese la cédula del paciente: ")
          tipo_implante = ProtesisCadera  # Tipo de implante a asignar, podrías cambiarlo según el tipo deseado
          fecha_implantacion = datetime.datetime.now()
          medico_responsable = input("Ingrese el nombre del médico responsable: ")
          estado = input("Ingrese el estado del implante: ")
          base.asignar_implante_a_paciente(cedula_paciente, tipo_implante, fecha_implantacion, medico_responsable, estado)
         

          #pacientes.agregarProtesis(Paciente)

        elif menu =="5":
            pass
        elif menu=="6":
           break
        else:
            print("Salió del sistema.")
            break

if __name__ == '__main__':
    main()
#