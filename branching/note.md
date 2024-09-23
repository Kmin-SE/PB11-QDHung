## Cách biểu diễn thuật toán

1. Ngôn ngữ tự nhiên
2. Lưu đồ
3. Mã giả (pseudo-code)

## Cho nhập vào 3 số nguyên. Hãy in ra màn hình các số âm.

Input: a, b, c = 1, -2, -3
Output: -2, -3

Nếu số đó âm thì in ra
a, b, c = -1, 3, -2
Version 1:
```
if a < 0:
    print(a)
    if b < 0:
        print(b)
        if c < 0:
            print(c)
    else:
        if c < 0:
            print(c)
else:
    if b < 0:
        print(b)
        if c < 0:
            print(c)
    else:
        if c < 0:
            print(c)
```

if A:
    X
    Y
else:
    Z
    Y

Rút lại:
if A:
    X
else:
    Z

Y

Version 2
```
    if a < 0:
        print(a)
    if b < 0:
        print(b)
    if c < 0:
        print(c)
```

Đếm
```
    dem = 0
    if a < 0:
        dem += 1
    if b < 0:
        dem += 1
    if c < 0:
        dem += 1
```

Tổng âm
```
    tongAm = 0
    if a < 0:
        tongAm += a
    if b < 0:
        tongAm += b
    if c < 0:
        tongAm += c
```

Ngày tháng năm hợp lệ

Nếu năm hợp lệ và tháng hợp lệ và ngày hợp lệ thì hợp lệ

max_ngay = 0

if thang in [1, 3, ...]:
    max_ngay = 31
elif thang in [4, 6, ..,]:
    max_ngay = 30
else:
    if nam nhuận:
        max_ngay = 29
    else:
        max_ngay = 28

if nam > 0 and thang >= 1 and thang <= 12 and ngay >= 1 and ngay <= max_ngay:
    print("Valid")
else:
    print("Unvalid")