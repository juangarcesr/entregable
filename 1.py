#se crea el repositorio
class Sistema():
  def __init__(self):
    pass

  #Agregar nuevo implante. \n Editar. \n  Visualizar inventario. \n Eliminar.
  #Registro de Pacientes y Asignación de Implantes: El sistema debe permitir asociar
  #implantes específicos a pacientes, registrando información sobre la fecha de implantación,
  #el médico responsable y el estado del implante en el paciente.
  #Seguimiento de Implantes: Debe ser posible realizar un seguimiento de la vida útil de los
  #implantes, incluyendo fechas de revisión y mantenimiento.

class Implante():
  def __init__(self):
    pass

class ProtesisCadera(self):
  def __init__(self):
    self.__Material = material
    self.__Fijación = fijación
    self.__Tamaño = tamaño

  def verMaterial (self):
    return self.__nombre
  def asignarMaterial (self, Material):
    self.__Material = Material

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación

  def verTamano (self):
    return self.__Tamaño
  def asignarTamano (self, Tamaño):
    self.__Tamaño = Tamaño


class StentCoronario(self, Longitud, diametro, material):
  def __init__(self):
    self.__Longitud = longitud
    self.__Diametro = Diametro
    self.__Material = material

  def verLongitud (self):
    return self.__Longitud
  def asignarLongitud (self, Longitud):
    self.__Longitud = Longitud

  def verDiametro (self):
    return self.__Diametro
  def asignarDiametro (self, Diametro):
    self.__Diametro = Diametro

  def verMaterial (self):
    return self.__nombre
  def asignarMaterial (self, Material):
    self.__Material = Material

class ImplanteDental(self, material, fijacion, tamano):
  def __init__(self):
    self.__Material = material
    self.__Fijación = fijacion
    self.__Tamaño = tamano

  def verMaterial (self):
    return self.__nombre
  def asignarMaterial (self, Material):
    self.__Material = Material

  def verFijacion (self):
    return self.__Fijación
  def asignarFijacion (self, Fijación):
    self.__Fijación = Fijación

  def verTamano (self):
    return self.__Tamaño
  def asignarTamano (self, Tamaño):
    self.__Tamaño = Tamaño

class Marcapasos(self, electrodos,Tipo):
  def __init__(self):
    self.__NumeroElectrodos = electrodos
    self.__Tipo = 0
    self.__FrecuenciaEstimulación = Frecuencia

  def verNumElectrodos (self):
    return self.__NumeroElectrodos
  def asignarNumElectrodos (self, numElectrodos):
    self.__NumeroElectrodos = NumeroElectrodos

  def verTipo (self):
    return self.__Tipo
  def asignarTipo (self, Tipo):
    self.__Tipo = Tipo

  def verFrecuenciaEstimulacion(self):
    return self.__FrecuenciaEstimulacion
  def asignarFrecuenciaEstimulacion(self, frecuenciaEstimulacion):
    self.__FrecuenciaEstimulacion = Frecuencia

class ProtesisRodilla():
  def __init__(self):
    pass