def tao_tuple_tu_list(lst):
    return tuple(lst)

#Nhap danh sach tu nguoi dung va xu ly chuoi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List:", numbers)
print("Tuple tu List:", my_tuple)