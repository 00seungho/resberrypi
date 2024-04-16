import RPi.GPIO as GPIO
import time
import threading
import requests
from datetime import datetime,timedelta
import smbus

import json
SW1_PIN = 4
GPIO.setmode(GPIO.BCM)

if __name__ == "__main__":
 
    GPIO.setup(SW1_PIN,GPIO.IN)

    whater = "맑음"
    def load_whater():
        today = datetime.today().strftime("%Y%m%d%H") if datetime.today().minute > 40 else (datetime.today() - timedelta(hours=1)).strftime("%Y%m%d%H")
        hour = today[8:]
        today = today[:8]
        url = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
        params ={'serviceKey' : "NiGhn1xzYgu3Jk2dfWcsdseqg0Iufba/pRhl0nHbuNsDK8poZ0xTKBgyTNO0mzWieKL4TtLgCY0oTGD15kFlWw==", 
                'pageNo' : '1',  
                'numOfRows' : '1000', 
                'dataType' : 'JSON', 
                'base_date' : today, 
                'base_time' : str(int(hour)*100+40), 
                'nx' : '60', 
                'ny' : '126'}
        try:
            
            response = requests.get(url, params=params)
            items = response.json()["response"]["body"]["items"]["item"]
            for idx, item in enumerate(items):
                if item["category"] == "PTY":#PTY가 눈오는지 비오는지 나타냄
                    rain = items[idx]
            if rain["obsrValue"] == "0":
                print("맑음")
                whater = "맑음"
            else:
                print("비나 눈옴")
                whater = "안맑음"
        except:
            GPIO.cleanup()
        finally:
            threading.Timer(40 * 60, load_whater).start()  # 40분마다 함수 호출
    load_whater()

    while True:
        time.sleep(1)
        if GPIO.input(SW1_PIN) == 0:
            print(whater)

        