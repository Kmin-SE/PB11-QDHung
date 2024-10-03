def test(x): # x = a (ref)
    x[0] = "mango"

a = ["apple", "banana", "cherry"]
test(a)
print(a)

