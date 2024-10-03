def test(a):
    return a + 10

b = test(5)
print(b)

x = lambda a : a + 10
b = x(5)
print(b)

y = lambda a, b : a * b
print(y(5, 6))