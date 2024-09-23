Sinh viên
- Mã số
- Tên
- Điểm

Chọn cấu trúc dữ liệu

Giải pháp 1: Biến
- id
- name
- grade

Chức năng xuất thông tin sinh vien
output(id, name, grade)

Giải pháp 2: List
dssv = [(id0, name0, grade0), (id1, name1, grade1), ...]
name0 = dssv[0][1]

dsid = [id0, id1, ...]
dsname = [name0, name1, ...]
dsgrade = [grade0, grade1, ...]
Thông tin sinh viên 0: dsid[0], dsname[0], dsgrade[0]

td = {"id": 0, "name": "A", "grade": 0}
td["id"] => 0
td["name"] => "A"

dssv = [
    {"id": 0, "name": "A", "grade": 0},
    {"id": 1, "name": "B", "grade": 1},
    ...
]

dssv[1]["name"] => "B"


Lớp: Thuộc tính (attribute / property)
Đối tượng thuộc về lớp


Hướng đối tượng:
- Tính đóng gói, che chắn và bảo bọc dữ liệu



class PhanSo:

Nhap
Xuat
Cong
