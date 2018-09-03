import time
import serial
import math


ser = serial.Serial()

ser.baudrate = 115200
ser.port = 'COM4'
ser.open()

time.sleep(2)
ser.write(b'@')
time.sleep(2)
ser.write(b'p')
time.sleep(2)
ser.write(b'9')
time.sleep(2)


while True:
    ser.write(b'v')
    ser.write(b'0')
    time.sleep(1)
    ser.write(b'v')
    ser.write(b'100')
    time.sleep(1)
