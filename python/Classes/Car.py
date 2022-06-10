class Car(object):
  def __init__(self, name, maker):
    self.name = name
    self.maker = maker

  """
  Get Make of Car
  """
  def getMaker(self):
    return self.maker
    
  """
  Get Name of Car
  """
  def getName(self):
    return self.name

class Sedan(Car):
  def __init__(self, maker, model, color, driveType, name = 'Unamed'):
    super().__init__(name, maker)
    self.model = model
    self.color = color
    self.driveType = driveType
  
  """
  Get Model of Car
  """
  def getModel(self):
    return self.model

  """
  Get Color of Car
  """
  def getColor(self):
    return self.color

  """
  Get Drive Type of Car
  """
  def getDrivetype(self):
    return self.driveType
  
  """
  Print out Vehicle Information Nicely
  """
  def getMyCar(self):
    return f'\n------Car------\nMaker: {self.maker}\nName: {self.name}\nModel: {self.model}\nColor: {self.color}\nDrive Type: {self.driveType}'