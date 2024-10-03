def func(a): # Pass by value
    print(a) # 5
    a = 1

a = 5
func(a)

print(a)