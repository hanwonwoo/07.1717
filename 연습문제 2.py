#문자메세지 길이
#메세지 길이가 20이하이면 50원
#20원을 초과하면 100원




text = input("문자메세지를 입력하세요:")

def aa(a):
    if len(a) <= 20:
        print("50원")
    else:
        print("100원")
        result = a
        return result
aa(text)


