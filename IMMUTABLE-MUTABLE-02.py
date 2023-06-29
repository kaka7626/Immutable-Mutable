danhSach = ['long', 'Ezzra', 'Arkana', 'Wiktor'] # list là kiểu dữ liệu thay đổi được (mutable)
danhSach02 = danhSach

danhSach02.append('Hoàng')

print(danhSach) # list không truyền hẳn dữ liệu vào biến, mà chỉ truyền bản sao của nó thôi
print(danhSach02) 
# vì thế khi thay đổi dữ liệu của danhSach02 thì danhSach cũng thay đổi theo do đã thay đổi dữ liệu từ bản gốc