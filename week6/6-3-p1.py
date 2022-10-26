import RPi.GPIO as GPIO
import time
import getch


PWMA, AIN1, AIN2 = 18, 22, 27
PWMB, BIN1, BIN2 = 23, 25, 24

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

def L(dutycycle):
    if(dutycycle >= 0):
        GPIO.output(AIN1, 0)
        GPIO.output(AIN2, 1)
    else:
        GPIO.output(AIN1, 1)
        GPIO.output(AIN2, 0)
    L_Motor.ChangeDutyCycle(abs(dutycycle))

def R(dutycycle):
    if(dutycycle >= 0):
        GPIO.output(BIN1, 0)
        GPIO.output(BIN2, 1)
    else:
        GPIO.output(BIN1, 1)
        GPIO.output(BIN2, 0)
    R_Motor.ChangeDutyCycle(abs(dutycycle))

def LR(ld, rd):
    L(ld)
    R(rd)

try:
    while True: # 무한 반복
        char = getch.getch()

        if(char == 'w'): # 앞
            LR(100, 100)
            print("전진") # 출력
        if(char == 's'): # 뒤
            LR(-100, -100)
            print("후진") # 출력
        if(char == 'a'): # 좌
            LR(-100, 100)
            print("좌회전") # 출력
        if(char == 'd'): # 우
            LR(100, -100)
            print("우회전") # 출력

        time.sleep(0.3) # 0.3초 대기
        LR(0, 0) # 정지
except KeyboardInterrupt: # 인터럽트 처리
    pass

GPIO.cleanup() # 핀 설정 초기화