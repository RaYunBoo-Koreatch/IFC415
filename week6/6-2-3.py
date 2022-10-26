import RPi.GPIO as GPIO
import time

pinSwitch = 5 # GPIO5
pinBuzzer = 12 # GPIO12
frequency = (349, 349)

GPIO.setmode(GPIO.BCM) # 핀번호를 BCM(GPIO)기준으로
GPIO.setup(pinSwitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # INPUT, PULLDOWN 으로 초기화
GPIO.setup(pinBuzzer, GPIO.OUT) # OUTPUT으로 초기화

p = GPIO.PWM(pinBuzzer, frequency[0]) # pwm 호출

try:
    lastSwitch = 0 # 이전 상태를 보관
    while True: # 무한 반복
        swVal = GPIO.input(pinSwitch) # 버튼 입력을 받고
        
        if(lastSwitch == 0 and swVal == 1): # Rising에만 동작
            for freq in frequency:
                p.ChangeFrequency(freq) # 음계를 설정
                p.start(50) # duty cycle = 50%
                time.sleep(0.2) # 0.2초 대기
                p.stop() # 부저 정지
                time.sleep(0.3) # 0.3초 대기
        
        lastSwitch = swVal # 이전 상태 업데이트
        time.sleep(0.05) # 채터링 감소
except KeyboardInterrupt: # 인터럽트 처리
    pass

GPIO.cleanup() # 핀 설정 초기화