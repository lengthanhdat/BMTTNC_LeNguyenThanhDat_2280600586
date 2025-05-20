def dao_nguoc_list(lst):
    return lst[::-1]
#Nhap danh sach tu nguoi dung va xu ly chuoi
inmput_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inmput_list.split(',')))
#Su dung ham va in ra ket qua   
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi dao nguoc:", list_dao_nguoc)