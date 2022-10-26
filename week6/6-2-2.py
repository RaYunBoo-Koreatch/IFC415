import RPi.GPIO as GPIO
import time

pinBuzzer = 12 # GPIO12
frequency = (349, 349)

GPIO.setmode(GPIO.BCM) # 핀번호를 BCM(GPIO)기준으로
GPIO.setup(pinBuzzer, GPIO.OUT) # OUTPUT으로 초기화

p = GPIO.PWM(pinBuzzer, frequency[0]) # pwm 호출

try:
    for freq in frequency:
        p.ChangeFrequency(freq) # 음계를 설정
        p.start(50) # duty cycle = 50%
        time.sleep(0.2) # 0.2초 대기
        p.stop() # 부저 정지
        time.sleep(0.3) # 0.3초 대기
        
except KeyboardInterrupt: # 인터럽트 처리
    pass

p.stop() # 부저 정지
GPIO.cleanup() # 핀 설정 초기화