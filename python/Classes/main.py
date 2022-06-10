from Car import *

# Run main.py and these methods will run
if __name__ == "__main__":
  toyota = Sedan("toyota", "corolla sport", "red", "AWD", "My Bitch")
  print(toyota.getMaker())
  print(toyota.getName())
  print(toyota.getModel())
  print(toyota.getColor())
  print(toyota.getDrivetype())
  print(toyota.getMyCar())