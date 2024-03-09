#se crea el repositorio
class Sistema():
  def __init__(self):
    def __init__(self):
        self.inventario = []

    def agregar_implante(self, implante):
        self.inventario.append(implante)

    def eliminar_implante(self, implante):
        self.inventario.remove(implante)

    def editar_implante(self, implante, atributo, valor):
        setattr(implante, atributo, valor)

    def visualizar_inventario(self):
        for implante in self.inventario:
            print(implante)

 #agregar nuevos implantes, eliminarlos, editar su información y visualizar el inventario completo.

class Implante():
    def __init__(self, tipo, material, tamaño):
        self.__tipo = tipo
        self.__material = material
        self.__tamaño = tamaño

    def verTipo(self):
       return self.__tipo
    def verMaterial(self):
       return self.__material
    def verTamaño(self):
       return self.__tamaño
    
    def asignarTipo(self,t):
       self.__tipo=t
    def asignarTamaño(self,ta):
       self.__tamaño=ta
    def asignarMaterial(self,m):
       self.__material=m


    def __str__(self):
        return f'Tipo: {self.tipo}, Material: {self.material}, Tamaño: {self.tamaño}'

class ProtesisCadera(Implante):
  def __init__(self,material,fijacion,tamaño):
    super().__init__(material,tamaño)
    self.__Fijación = fijacion

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación

class StentCoronario(Implante):
  def __init__(self,material,longitud,diametro,tamaño):
     super().__init__(material,tamaño)
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
  
  def __init__(self,material,fijacion,forma):
    super().__init__(material)   
    self.__Fijación = fijacion
    self.__forma=forma

  def verForma (self):
    return self.__forma
  def asignarFijacion (self, Fo):
    self.__forma=Fo 

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación

class Marcapasos(Implante):
  def __init__(self,NumElectrodos,tipo,frecuenciasEstimulacion):
    super().__init__(tipo)
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
  def __init__(self,material,fijacion,tamaño):
    super().__init__(material,tamaño)
    self.__Fijación = fijacion

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación
  
