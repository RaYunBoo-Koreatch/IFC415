import RPi.GPIO as GPIO
import time

pinBuzzer = 12 # GPIO12
frequency = (262, 294, 330, 349, 392, 440, 494, 523) # 도~도

GPIO.setmode(GPIO.BCM) # 핀번호를 BCM(GPIO)기준으로
GPIO.setup(pinBuzzer, GPIO.OUT) # OUTPUT으로 초기화

p = GPIO.PWM(pinBuzzer, frequency[0]) # pwm 호출

try:
    while True: # 무한 반복
        for freq in frequency: # 음계를 순서대로
            p.ChangeFrequency(freq) # 음계를 설정
            p.start(50) # duty cycle = 50%
            time.sleep(0.5) # 0.5초 대기
            p.stop() # 부저 정지
            time.sleep(0.5) # 0.5초 대기
        
except KeyboardInterrupt: # 인터럽트 처리
    pass

p.stop() # 부저 정지
GPIO.cleanup() # 핀 설정 초기화