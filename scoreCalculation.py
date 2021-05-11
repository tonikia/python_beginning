"""python101 = int(input("학점을 입력하세요: "))
if python101 >= 90:
    print("학점: A")
elif python101 >= 80:
    print("학점: B") 
elif python101 >= 70:
    print("학점: C") 
elif python101 >= 60:
    print("학점: D")
else:
    print("학점: F")
print("수고하셨습니다.")"""

scoreMath = int(input("수학 점수를 입력하세요: "))
scoreEng = int(input("영어 점수를 입력하세요: "))
scoreAvr = (scoreMath + scoreEng)/2

if scoreAvr >= 90:
    print("수학과 영어 평균 학점은 A입니다.")
elif scoreAvr >= 80:
    print("수학과 영어 평균 학점은 B입니다.") 
elif scoreAvr >= 70:
    print("수학과 영어 평균 학점은 C입니다.") 
elif scoreAvr >= 60:
    print("수학과 영어 평균 학점은 D입니다.")
else:
    print("수학과 영어 평균 학점은 F입니다.")

