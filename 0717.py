#구구단 2-9단을 출력하라.
#
# for j in range(2,10 ):
#     for i in range(1, 10):
#         print(j,"x", i, "=", i * j )

#구구단 함수를 작성하시오.
#구구단 화면에 출력하는 함수

 # def print_mul_table(x):
 #     print(x)
 #
 #  for i in range(1,10):
 #         print("3 x ", i , "=", 3 * i)
 #
#
# def print_mul_table(x):
#     result = x
#     return result
#
#     for i in range(1,10):
#         print("3 x", i, "=", 3 * i)
# # print_mul_table(3)

def print_mul_table(x):
    for i in range(1, 10):
        print(x, "x", i, "=", x * i)

print_mul_table(6)





#
# def sum_2(a):
#     for q in range (1,10):
#         print(a, "x", q, "=", a *q)
# sum_2(4)