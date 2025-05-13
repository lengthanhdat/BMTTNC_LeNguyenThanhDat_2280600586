#Ham kiem tra so nhi phan co chia het cho 5 khong
def chia_het_cho_5(so_nhi_phan):
    #Chuyen so nhi phan sang so thap phan
    so_thap_phan = int(so_nhi_phan, 2)
    #Kiem tra xem so thap phan co chia het cho 5 khong 
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#Nhap chuoi so nhi phan tu nguoi dung
chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan(phan tach boi dau phay): ")