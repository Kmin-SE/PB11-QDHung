

def interchange_sort(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                # temp = a[i]
                # a[i] = a[j]
                # a[j] = temp
                a[i], a[j] = a[j], a[i]

a = [5, 8, -2, -5, 1, 8, -4]
# a = [-2, 8, 5, -5, 1, 8, -4]
interchange_sort(a)
print(a)