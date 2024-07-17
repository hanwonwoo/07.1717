#평균값 구하는 함수 작성
#리스트 길이는 매번 달라짐
#sum()함수를 사용할 수 없다

# def list_ave(x):
#     result=0
#     for i in x:
#         result= result + 1
#     print(result/len(list))
# list = [10, 5, 5, 15, 6, 5, 8]
# list_ave(list)

var = [1,2,3,4,5,6,7,8,9,10]
def mean_list(x):
    result = 0
    for i in x :
        result = result + i
    avg = result/len(x)
    return avg

var = list(range(2, 99999))
print(mean_list(var))




