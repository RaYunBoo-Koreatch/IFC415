import RPi.GPIO as GPIO
import time

PWMA, AIN1, AIN2 = 18, 22, 27
PWMB, BIN1, BIN2 = 23, 25, 24
def L(dutycycle):
    L_Motor.ChangeDutyCycle(dutycycle)
def R(dutycycle):
    R_Motor.ChangeDutyCycle(dutycycle)


GPIO.setmode(GPIO.BCM) # 핀번호를 BCM(GPIO)기준으로
GPIO.setup(PWMA, GPIO.OUT) # OUTPUT으로 초기화
GPIO.setup(AIN1, GPIO.OUT) # OUTPUT으로 초기화
GPIO.setup(AIN2, GPIO.OUT) # OUTPUT으로 초기화
GPIO.setup(PWMB, GPIO.OUT) # OUTPUT으로 초기화
GPIO.setup(BIN1, GPIO.OUT) # OUTPUT으로 초기화
GPIO.setup(BIN2, GPIO.OUT) # OUTPUT으로 초기화

GPIO.output(AIN1, 0)
GPIO.output(AIN2, 1)
GPIO.output(BIN1, 0)
GPIO.output(BIN2, 1)

L_Motor = GPIO.PWM(PWMA, 500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB, 500)
R_Motor.start(0)

try:
    while True:
        L(50)
        R(50)
        time.sleep(1.0)
        
        L(0)
        R(0)
        time.sleep(1.0)

except KeyboardInterrupt: # 인터럽트 처리
    pass

GPIO.cleanup() # 핀 설정 초기화