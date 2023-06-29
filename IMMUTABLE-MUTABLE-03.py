def ham(parameter):
    parameter.append('Ezzra')

long = [1, 2, 3, 4]
ham(long) # đáng lẽ ở đây biến local phải bị hủy do hàm đã return kết quả
print(long) # thì list long phải print ra là [1, 2, 3, 4], nhưng list ở đây chỉ là bản sao 
            # thay đổi ở đây là thay đổi dữ liệu ở bản gốc, nên mới print ra [1, 2, 3, 4, 'Ezzra']