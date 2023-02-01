#This code include print sentences in Spanish but it can be customized.
import time
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(4)

while True:
    try:
        t = dhtDevice.temperature

        if t < 5:
            print("Hay demasiado frio y peude haber heladas o nievem, estamos a ({:.1f}C)".format(t))
        elif t >= 5 and t < 10:
            print("En estos momentos hace frio, temperaturas baja de ({:.1f}C)".format(t))
        elif t >= 10and t < 15:
            print("Ahora mismo se las temperaturas son algo bajas pero no hace mucho frio, hay ({:.1f}C)".format(t))
        elif t >= 15 and t < 20:
            print("La temperatura actual es estable, no hace frio ni tampoco mucho calor, hay ({:.1f}C)".format(t))
        elif t >= 20 and t < 26:
            print("En estos momemntos hay una temperatura agradable, exactamente ({:.1f}C)".format(t))
        elif t >= 26 and t < 31:
            print("Segun los datos la temperatura es alta pero sin riesgo, hay ({:.1f}C)".format(t))
        elif t >= 31 and t < 36:
            print("La temperatura es elevada,hay ({:.1f}°C)".format(t))
        elif t >= 36 and t < 40:
            print("Hace demasiado calor, hay exactamente({:.1f}C)".format(t))
        else:
            print("Atencion,PELIGRO!!!la tmeperatura actual es un riesgo importante para la salaud y el entorno, se recomienda no salir al exterior, hay ({:.1f}C)".f$
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(2.0)


