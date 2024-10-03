# Sử dụng lambda trong hàm tự định nghĩa
# def apply_operation(x, y, operation): # x = 5, y = 3, 
#     # operation =  lambda a, b: print(a+b)
#     operation(x, y)

# apply_operation(5, 3, lambda a, b: print(a+b))
# apply_operation(5, 3, lambda a, b: print(a-b))


# def apply_operation(x, y, operation): # x = 5, y = 3, 
#     # operation =  lambda x, y: x + y
#     return operation(x, y)

# # Sử dụng hàm apply_operation với lambda để thực hiện các phép tính
# addition = apply_operation(5, 3, lambda x, y: x + y)
# subtraction = apply_operation(11, 7, lambda x, y: x - y)

# print(addition)     # Kết quả: 8
# print(subtraction)  # Kết quả: 4


def my_filter(a, tieu_chi):
    b = []
    for x in a:
        if tieu_chi(x) == True:
            b.append(x)
    return b

c = my_filter([3, 4, 5, 6, 7], lambda x: x % 2 != 0)
print(c)