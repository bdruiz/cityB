import paho.mqtt.client as paho
import sys
import serial
broker="127.0.0.1"
port=1883

PuertoSerie = serial.Serial('/dev/ttyACM0', 9600)


def on_publish(client,userdata,result):
    print("data published \n")

def main():
    while True:
        sArduino = PuertoSerie.readline()
        print "Valor Arduino: " + sArduino.rstrip('\n')
        client1= paho.Client("Gateway 01 Rpi")
        client1.on_publish = on_publish
        client1.connect(broker,port)
        client1.publish(sArduino)
        sArduino.close()
#    client1.loop_forever()


if __name__ == '__main__':
    main()

sys.exit(0)





