import math
gia_tien_dien = 7000
t = float(input("Thời gian sử dụng điện là: "))
if t > 0 :
    P = U * I
    # Tính năng lượng tiêu thụ (kWh)
    E = (P * t) / (1000 * 3600)
    # Tính tiền điện phải trả
    tien_dien = E * gia_tien_dien
    print(f"TIỀN ĐIỆN CỦA BAN LÀ: {tien_dien:2f} ")
else :
    print(" thoi gian khong the am ")