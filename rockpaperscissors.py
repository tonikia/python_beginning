#가위바위보게임
import random #랜덤함수로 난수 불러오기

#컴퓨터 설정
player = input("(가위, 바위, 보) 중 하나를 선택하세요: ")
number = random.randint(0, 2) #0, 1, 2중 하나 생성
if number == 0:
    computer = "가위"
elif number == 1:
    computer = "바위"
elif number == 2:
    computer = "보"
print("사용자: ", player, ", 컴퓨터: ", computer) 

#승패 설정
if player == computer:
    print("비겼음!")
if player == "가위":
    if(computer == "바위"):
         print("졌음!")
    elif(computer == "보"):
        print("이겼음!")
if player == "바위":
    if(computer == "보"):
         print("졌음!")
    elif(computer == "가위"):
        print("이겼음!")
if player == "보":
    if(computer == "가위"):
         print("졌음!")
    elif(computer == "보"):
        print("이겼음!")