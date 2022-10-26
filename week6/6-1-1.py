import RPi.GPIO as GPIO
import time

pinSwitch = 5

GPIO.setmode(GPIO.BCM) # 핀번호를 BCM(GPIO)기준으로
GPIO.setup(pinSwitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # INPUT, PULLDOWN 으로 초기화

try:
    lastSwitch = 0 # 이전 상태를 보관
    while True: # 무한 반복
        swVal = GPIO.input(pinSwitch) # 버튼 입력을 받고
        
        if(lastSwitch == 0 and swVal == 1): # Rising에만 동작
            print("click") # 출력
        
        lastSwitch = swVal # 이전 상태 업데이트
        
        time.sleep(0.05) # 채터링 감소
except KeyboardInterrupt: # 인터럽트 처리
    pass

GPIO.cleanup() # 핀 설정 초기화