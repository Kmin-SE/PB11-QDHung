# a = [1, 2, 3, 4]
# b = [4, 7, 10, 13]

# b[i] = a[i] * 3 + 1

def mapping(a, exp):
    b = []
    for value in a:
        b.append(exp(value))
    return b

a = [1, 2, 3, 4]
b = mapping(a, lambda v : v*3+1)
c = mapping(a, lambda v : v*2-3)
print(c)


