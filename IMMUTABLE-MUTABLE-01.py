name = 'Ezzra'
# for letter in name:
#     print(letter)

print(name[2])
# name[2] = 'X' lỗi vì string là kiểu dữ liệu không thay đổi tại chỗ (immutable) 
# chỉ có thể thay đổi bằng đặt biến mới 

newName = name[0:2] + 'x' + name[3:5] # có thể đổi dữ liệu string bằng slice nhưng lằng nhằng vcl
print(newName) 