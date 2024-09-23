k = 7
s = ""
for i in range(k):
    if i % 2 == 0:
        s += "* "
    else:
        s += "$ "

print(s)