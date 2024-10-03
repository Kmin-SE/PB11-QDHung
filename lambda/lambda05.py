# Sắp xếp danh sách các tuple theo phần tử thứ 2
pairs = [(1, 5), (3, 2), (7, 8), (4, 3)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Kết quả: [(3, 2), (4, 3), (1, 5), (7, 8)]