def func(a): # Pass by reference
    a[0] = 1

a = [5, 6, 7]
func(a)

print(a)