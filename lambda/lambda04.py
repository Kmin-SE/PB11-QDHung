# Lọc các số lẻ từ danh sách
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Kết quả: [1, 3, 5, 7, 9]