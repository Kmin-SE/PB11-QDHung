# In số lẻ từ n => 1

# n = 8
# i = 1
# while n >= i:
#     if n % 2 == 0:
#         print(n - 1)
#     else:
#         print(n)
#     n = n - 2

# Cách 2

# n = 9
# i = None

# if n % 2 == 0:
#     i = n - 1
# else:
#     i = n

# while i >= 1:
#     print(i)
#     i -= 2

n = 9
i = n

while i >= 1:
    if i % 2 == 1:
        print(i)
    i -= 1