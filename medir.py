
import time
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(4)

while True:
    try:
        t = dhtDevice.temperature
        if t < 5:
            print("Atención es posible riesgo de helada o nieve, temperatura muy baja({:.1f}°C)".format(t))
        elif t >= 5 and t < 10:
            print("En estos momentos hace frío, temperatura baja de ({:.1f}°C)".format(t))
        elif t >= 10and t < 15:
            print("Ahora mismo se nota cierta bajada de termometro, hay ({:.1f}°C)".format(t))
        elif t >= 15 and t < 20:
            print("La temperatura actual es agradable de ({:.1f}°C)".format(t))
        elif t >= 20 and t < 26:
            print("En estos moemntos hay una temperatura fantástica y primaveral, exactamente ({:.1f}°C)".format(t))
        elif t >= 26 and t < 31:
            print("En estos moentos la temperatura es alta, hay ({:.1f}°C)".format(t))
        elif t >= 31 and t < 36:
            print("La temperatura ha subido mucho, es necesario tomar precaución, hay ({:.1f}°C)".format(t))
        elif t >= 36 and t < 40:
            print("La tempera actual es elevada y se considera cierto riesgo para la salud, tenga cuidado, hay exactamente({:.1f}°C)".format(t))
        else:
            print("Atención,PELIGRO!!!la tmepoeratura actual es demasiado elevada, se recomienda no salir al exterior, hay ({:.1f}°C)".format(t))
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(2.0)

