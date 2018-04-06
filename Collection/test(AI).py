import threading
import time
import json

g_Balcony_Windows = False
g_AI_Mode = False

def update_scheduler():
    global g_Balcony_Windows
    while True:
        if g_AI_Mode == False:
            continue
        else:
            AI_time = time.localtime(time.time())
            if AI_time[4] == 0 and AI_time[5] == 50:
                g_Balcony_Windows = not g_Balcony_Windows
                print("발코니를 열겠습니다.")
                time.sleep(1)

t = threading.Thread(target=update_scheduler)
t.daemon = True
t.start()

while True:
    print("메뉴를 선택하세요")
    print("1. 장비 상태 조회")
    print("2. 인공지능 모드 변경")
    print("3. 종료")

    menu_num = int(input("메뉴 입력: "))
    if(menu_num==1):
        print("발코니(베란다) 창문: ",end='')
        if g_Balcony_Windows==True: print("열림")
        else: print("닫힘")
    elif(menu_num==2):
        print("인공지능 모드: ", end='')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode==True: print("작동")
        else: print("정지")
    else: break

# AI_time = time.localtime(time.time())
# if AI_time[4] == 39:
#     print("OK")