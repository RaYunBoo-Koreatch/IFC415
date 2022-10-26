# -*- coding: utf8 -*-
import RPi.GPIO as GPIO
import time
import serial

pinLeds = (26, 16, 21, 20) # 시계방향으로 핀 목록을 작성

GPIO.setmode(GPIO.BCM) # GPIO번호를 BCM기준으로, BOARD는 보드에 핀순서
for pin in pinLeds:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW) # 각 핀을 OUTPUT, LOW로 초기화


bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

def readAll(serial):
    while serial.in_waiting:
        print(bleSerial.readline().decode('utf-8'), end='')

try:
    while True:
        readAll(bleSerial)
        
except KeyboardInterrupt:
    pass

bleSerial.close()
GPIO.cleanup() # GPIO 출력 설정 초기화
