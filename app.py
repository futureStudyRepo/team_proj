# app.py
import time
import datetime

print("서버 구동 시작!")

while True:
    with open("server.log", "a") as f:
        # 10초마다 현재 시간과 버전 정보를 로그 파일에 씁니다.
        f.write(f"서버 정상 작동 중 (버전 1) - {datetime.datetime.now()}\n")
    time.sleep(10)