#basic
"""i=0
while i<5:
    print("Hello, Python!")
    i = i + 1 
print("반복이 종료되었습니다.")"""

#3배수 제외하고 1부터 100까지 합 구하기
"""total, i = 0, 0
for i in range(1, 101):
    if i % 3 == 0:
        continue
    total +=i
print("1 부터 100까지의 합계 (3 배수 제외): %d" %total)"""

#예제
"""for number in "123":
    print(number)"""

#정수들의 합: 1부터 n까지 더한 합을 계산하는 프로그램 작성 - FOR문 사용
#10까지 계산. 1부터 10까지 정수의 합 = 55
"""
max = int(input("어디까지 계산할까요?: "))
sum = 0
for i in range(1, max+1):
    sum += i

print("1부터", max,"까지의 정수의 합:",sum)
"""

#팩토리얼
#팩토리얼: n!은 1부터 n까지의 정수를 모두 곱한 것을 의미
#n! = 1 x 2 x .... x (n-1) x n
#정수를 입력하시오:10
#10!은 3628800.0이다.
"""
n = int(input("정수를 입력하시오: "))
fact = 1.0
for i in range(1, n+1):
    fact*=i
print(n,"!은", fact, "이다.")
"""

#자리수의 합
#정수 안의 각 자리수의 합을 계산하는 프로그램 작성
#예를들면 1234인 경우 1+2+3+4 계산
"""
number = 1234
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
print("자리수의 합은 %d입니다" %sum)
"""

#숫자 맞추기 게임
#시도 횟수 제공: 1부터 100 사이의 숫자를 맞추시오.
"""
import random

tries = 0
number = random.randint(1, 100)
print("1부터 100사이의 숫자를 맞추시오.")

while tries<10:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < number:
        print("낮음!")
    elif guess > number:
        print("높음!")
    else:
        break

if guess == number:
    print("축하하합니다. 시도횟수:", tries)
else:
    print("정답은", number)
    """

##커피 자판기
"""
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    """

#연습문제 1
"""
for x in range(1, 10):
    if x % 3 == 0:
        break
    print(x, end =" ")
print("끝")
"""

#연습문제 2
hap = 0
for i in range(1, 10):
    if i % 2 ==0:
        continue
    hap +=i
print(hap)