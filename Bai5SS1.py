# Phân tích 
# Các trường thông tin cần lấy từ người dùng là: mã bệnh nhân, họ tên bệnh nhân, tuổi bện nhân, nhiệt độ cơ thể, nhịp tim và cân nặng 
# Luồng ở đây là yêu cầu người dùng nhập vào sau đó lấy dữ liệu lưu vào các biến và ép kiểu phù hợp sau đó in ra phiếu điện tử 
# Thiết kế input phù hợp 
code_id = input("Nhập mã bệnh nhân của bạn: ")
name_patient = input("Nhập tên đầy đủ của bạn: ")
age_patient = int(input("Nhập tuổi của bạn(Vui lòng nhập số nguyên): "))
body_temperature = float(input("Nhập nhiệt độ cơ thể của bạn(Vui lòng nhập số thực): "))
heart_rate = int(input("Nhập nhịp tim của bản thân(Vui lòng nhập số nguyên): "))
weight = float(input("Nhập cân nặng của bạn(Vui lòng nhập số thực): ")) 

print("==================================================")
print("          PHIEU KHAM BENH DIEN TU")
print("==================================================")
print(f"họ và tên : {name_patient}")
print(f"Mã bệnh nhân     : {code_id}")
print(f"Tuổi             : {age_patient}")
print("----------------------------------------------")
print(f"Nhiệt độ cơ thể : {body_temperature} độ C")
print(f"Nhịp tim         : {heart_rate} BPM")
print(f"Cân nặng         : {weight} kg")
