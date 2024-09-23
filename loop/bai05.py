n = 7
if n % 2 == 0:
    for i in range(n-1, 0, -2):
        print(i)
else:
    for i in range(n, 0, -2):
        print(i)

n = 7
start = None
if n % 2 == 0:
    start = n - 1
else:
    start = n
for i in range(start, 0, -2):
        print(i)


# n = 8
# for i in range(n, 0, -2):
#     if i % 2 == 1:
#         print(i)
#     else:
#         print(i-1)

n = 8
for i in range(n, 0, -1):
    if i % 2 == 1:
        print(i)

