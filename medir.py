
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  if temperature is not None:
    if temperature < 5:
      print("Temperatura menor de 5 grados")
    elif temperature >= 5 and temperature < 10:
      print("Temperatura mayor de 5 y menor de 10")
    elif temperature >= 10 and temperature < 15:
      print("Temperatura mayor de 10 y menor de 15")
    elif temperature >= 15 and temperature < 20:
      print("Temperatura mayor de 15 y menor de 20")
    elif temperature >= 20 and temperature < 25:
      print("Temperatura mayor de 20 y menor de 25")
    elif temperature >= 25 and temperature < 30:
      print("Temperatura mayor de 25 y menor de 30")
    elif temperature >= 30 and temperature < 35:
      print("Temperatura mayor de 30 y menor de 35")
    elif temperature >= 35 and temperature < 40:
      print("Temperatura mayor de 35 y menor de 40")
    else:
      print("Temperatura mayor de 40")
  else:
    print("Error al obtener la temperatura")
