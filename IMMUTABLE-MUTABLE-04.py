import copy
long = [1, 2, 3, 4]
hoang = copy.deepcopy(long) # copy list y hệt long nhưng tạo ra 2 bản sao khác nhau từ nguồn
long.append('Wiktor')
print(long)
print(hoang) # vì thế khi print ra, list hoang không thay đổi như long