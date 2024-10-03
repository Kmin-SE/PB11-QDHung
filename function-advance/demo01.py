# def test(f): # Hàm có tham số là hàm
#     print('test')
#     # f()
#     # test3()

# def test2():
#     print('test2')

# def test3():
#     print('test3')

# # a = [1, 2]
# test(test3)

# # Lọc ra các số âm trong list
# def loc_am(a):
#     b = []
#     for value in a:
#         if value < 0:
#             b.append(value)
#     return b

# a = [1, -3, -4, 5]
# b = loc_am(a)
# print(b)

# # Lọc ra các số chẵn trong list
# def loc_chan(a):
#     b = []
#     for value in a:
#         if value % 2 == 0:
#             b.append(value)
#     return b

# a = [1, -3, -4, 5]
# b = loc_chan(a)
# print(b)

def loc(a, cond):
    b = []
    for value in a:
        if cond(value) == True:
            b.append(value)
    return b

# def kt_chan(value):
#     return value % 2 == 0

# def kt_am(value):
#     return value < 0

a = [1, -3, -4, 5]
b = loc(a, lambda v : v % 2 == 0)
print(b)