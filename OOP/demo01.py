class SinhVien:
    # Phương thức (method ~ function) khởi tạo
    # Magic method
    def __init__(self, id, name, grade=0):
        self.id = id
        self.name = name # public
        self.__grade = grade # private attribute

    # private method
    def __test(self):
        print('test')

    # public method
    def xuat(self):
        self.__test___()
        print('+ id:', self.id)
        print('+ name:', self.name)
        print('+ grade:', self.__grade)

    def xetQuaMon(self):
        if self.__grade >= 5:
            return True
        return False

    # Setter
    def ganDiem(self, diem_moi):
        if diem_moi >= 0 and diem_moi <= 10:
            self.__grade = diem_moi

    # Setter
    def layDiem(self):
        return self.__grade

a = SinhVien(0, "A", 7) # Đối tượng thuộc về lớp SinhVien
# a.grade = -1
# a.__grade = -1
# a.ganDiem(-1)
a.xuat()
a.__test___()
# print(a.xetQuaMon())

# b = SinhVien(1, "B")
# b.xuat()



