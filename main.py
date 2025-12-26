# Bước 1: Khởi tạo dữ liệu ban đầu
cot = int(input("Nhập số cột: "))
hang = int(input("Nhập số hàng: "))

# Tạo một mảng 2 chiều chứa toàn dấu "_"
so_do = [["_" for _ in range(cot)] for _ in range(hang)]

def hien_thi_so_do():
    print("\n---CHỖ NGỒI ---")
    for r in range(hang):
        for c in range(cot):
            print(so_do[r][c], end=" ")
        print() # Xuống dòng sau mỗi hàng

# Vòng lặp chính để chương trình chạy liên tục
while True:
    hien_thi_so_do()
    print("\n1: Đặt chỗ")
    print("2: Tổng số chỗ trống")
    print("3: Thoát")
    
    yeu_cau = int(input("Nhập yêu cầu của bạn: "))

    if yeu_cau == 1:
        # Bước 2: Xử lý đặt chỗ
        h_dat = int(input(f"Nhập hàng muốn đặt (0-{hang-1}): "))
        c_dat = int(input(f"Nhập cột muốn đặt (0-{cot-1}): "))
        
        # Kiểm tra xem chỗ đó đã đặt chưa
        if so_do[h_dat][c_dat] == "_":
            so_do[h_dat][c_dat] = "X"
            print("=> Đặt chỗ thành công!")
        else:
            print("=> Chỗ này đã có người ngồi rồi!")

    elif yeu_cau == 2:
        # Bước 3: Đếm số chỗ trống
        trong = sum(row.count("_") for row in so_do)
        print(f"=> Tổng số chỗ còn trống là: {trong}")

    elif yeu_cau == 3:
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ!")