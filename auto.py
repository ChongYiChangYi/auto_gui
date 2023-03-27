import pyautogui
import time

# print(pyautogui.position()) #내가 마우스 위치를 알려줌.

pos_next = (1489,726) # 화살표 위치를 적어놓으세요.
# pos_center = # 팝업창 확인
# pos_ans = # 무작위 답 하나 찍기
# 팝업창
while True:
    pyautogui.moveRel(-200,-200, 1) #연수 화면에 마우스 놓기
    pyautogui.moveTo(pos_next, duration=2) # x,y값으로 이동
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(180)




