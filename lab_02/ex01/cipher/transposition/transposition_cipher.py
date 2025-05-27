def decrypt(self, text, key):
    # số hàng tối thiểu
    n_rows = len(text) // key
    # số cột dư (số cột có 1 ký tự thêm)
    n_extra = len(text) % key
    
    cols = []
    start = 0
    for i in range(key):
        # Nếu cột i < n_extra thì cột này dài hơn 1 ký tự
        col_len = n_rows + 1 if i < n_extra else n_rows
        cols.append(text[start:start+col_len])
        start += col_len
    
    decrypted_text = ''
    # đọc theo hàng
    for row in range(n_rows + 1):
        for col in range(key):
            if row < len(cols[col]):
                decrypted_text += cols[col][row]
    
    return decrypted_text
