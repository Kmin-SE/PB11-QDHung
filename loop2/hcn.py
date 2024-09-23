# # Input
# k = 6

# # Process
# s = ""
# i = 1
# while i <= k:
#     s += "* "
#     i += 1

# # Output
# print(s)

# w, h = 5, 4

# for j in range(h):
#     for i in range(1, w+1):
#         if i < w:
#             print('* ', end='')
#         else:
#             print('* ', end='\n')

w, h = 5, 4

for j in range(h):
    for i in range(w):
        print('* ', end='')
    print('') # Xuống hàng

# O(hxw)


