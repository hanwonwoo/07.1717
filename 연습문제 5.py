#홀수/짝수 판별기 함수
#매개변수 입력 홀수 또는 짝수
#반환되는 값은 '홀수' 또는 '짝수'

def abc_1(x):
    result = ""
    if x % 2 == 1:
        result = "홀수입니다."
    else :
        result = "짝수입니다."
    return result
num=int(input("숫자를 입력하세요:"))
print(abc_1(num))

