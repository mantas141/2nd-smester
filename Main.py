from time import sleep
import serial

def readresponse():
        b = bytearray(b"                   ");
        ser.readinto(b)  #beware of timing issues here
        sleep(0.2)
        print(b)

def readbinaryresponse():
      #  b = bytearray(b"                   ");
        ser.readinto(b)  #beware of timing issues here
        sleep(0.2)
        print(b[0]*256 + b[1]   )
        #print(b[1])

#setup serial connection
ser = serial.Serial('COM3',115200,timeout=0.5)  # open serial port USB
#ser = serial.Serial('/dev/ttyAMA0',115200,timeout=0.5)  # open serial port on gpio
print(ser.name)         # check which port was really used
sleep(3)
#when the serial connection is initialized the usb-power is "flicked"
#causing the arduino to boot and thereby iddentify itself
readresponse()


print("ping client y gives")
ser.write(':'.encode('ascii'))
ser.write('y'.encode('ascii'))
ser.write('@'.encode('ascii'))
readresponse()

pos = 0

while True:
        for pos in range(0, 181):
                ser.write(':'.encode('ascii'))
                ser.write('y'.encode('ascii'))
                ser.write('s'.encode('ascii'))
                ser.write(pos)
                sleep(0.5)
        else:
                while pos > 0:
                        ser.write(':'.encode('ascii'))
                        ser.write('y'.encode('ascii'))
                        ser.write('s'.encode('ascii'))
                        ser.write(pos)
                        sleep(0.5)



#print("pin8 status")
#ser.write(':'.encode('ascii'))
#ser.write('y'.encode('ascii'))
#ser.write('r'.encode('ascii')) #reading the status of pin 8
#ser.write(b"\x08")
#readresponse()
#
#ser.write(':'.encode('ascii'))
#ser.write('y'.encode('ascii'))
#ser.write('o'.encode('ascii'))  #set pin 8 as output
#ser.write(b"\x08")
#
#print("Blinking pin8 status  ctrl-c to terminate  :-) ")