#학점 환산
#score를 입력 받아 학점 환산



var = int(input("점수을 입력하세요."))
def score(var) :
    result = ""
    if 81 <= var <= 100:
         result = "A"
    elif 61 <= var <= 80:
         result = "B"
    elif 41 <= var <= 60:
         result = "c"
    elif 21 <= var <= 40:
         result = "D"
    else:
        result = "F"
    return result
sc = int(input("점수을 입력하세요."))
res = score(sc)




