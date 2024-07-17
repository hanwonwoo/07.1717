# 판매가가 저장된 리스트
#부가세가 포함된 가격을 리스트로 반환
#numbers = [100, 200,300]
#print(VAT(numbers))
#출력 결과 [110,220,330]

var = [100,200,300]

def VAT(var):
    result_list = []
    for i in var:
        result_list.append(i * 1.1)
    return result_list

x = [100,200,300]
print(VAT(x))


