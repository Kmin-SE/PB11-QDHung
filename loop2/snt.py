# n = -1
# if n < 2:
#     print("Khong La SNT")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Khong La SNT")
#             break
#     else:
#         print("La SNT")

n = -1

flag = True
if n < 2:
    flag = False
else:
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break

if flag == True:
    print("La SNT")
else:
    print("Khong La SNT")

# Độ phức tạp thuật toán
# TT1: n - 2
# TT2: n + 100
# TT3: 2n
# O(n)

