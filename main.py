import csv

def read(file_name): #Tạo hàm đọc dữ liệu đầu vào
    danh_sach_hoc_sinh = []
    
    try:
        with open(file_name, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                hoc_sinh = {
                    'stt': row['STT'],
                    'msv': row['MSSV'],
                    'ho_ten': row['Họ và tên'],
                    'birth': row['Ngày sinh'],
                    'sex': row['Giới tính'],
                    'diem': {
                        'chuyen_can': float(row['Chuyên cần']),
                        'gk':   float(row['Giữa kỳ']),
                        'ck':  float(row['Cuối kỳ'])
                    }
                }
                danh_sach_hoc_sinh.append(hoc_sinh)
                
        print(f"--> Đã nhập thành công {len(danh_sach_hoc_sinh)} học sinh!")
        return danh_sach_hoc_sinh

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tên là '{file_name}'")
        return []
    except ValueError:
        print("Lỗi: Có dữ liệu điểm không phải là số trong file.")
        return []

# --- CHƯƠNG TRÌNH CHÍNH ---
ten_file = 'hocsinh.csv'
data_hoc_sinh = read(ten_file)

