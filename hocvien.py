# Xây dựng ứng dụng quản lý thông tin học viên.
# Một học viên bao gồm những thông tin:
# Mã số, họ tên, giới tính, tỉnh/thành phố, điểm thi lý thuyết,
# điểm thi thực hành (điểm thi cao nhất là 100, thấp nhất là 0).

# Người dùng có thể thực hiện các chức năng sau:
# 1 Thêm thông tin học viên vào bộ nhớ
# 2 Cập nhật thông tin học viên
# 3 Hiển thị danh sách tất cả học viên
# 4 Hiển thị danh sách học viên thi đỗ (Điểm trung bình >= 75)
# 5 Hiển thị danh sách học viên thi trượt (Điểm trung bình < 75)
# 6 Xóa thông tin của học viên
# Yêu cầu mở rộng (không bắt buộc):
# dữ liệu học viên có thể được xử lý qua file (đọc dữ liệu  cũ từ file và cập nhật dữ liệu mới vào file).


list_students = '''001,Nguyễn Văn A,Nam,Bình Định,80,90
002,Nguyễn Văn B,Nam,Bình Phước,60,80
003,Nguyễn Văn C,Nam,Bình Chánh,20,30'''

def show_menu():
    print('''Người dùng có thể thực hiện các chức năng sau:
1 Thêm thông tin học viên vào bộ nhớ
2 Cập nhật thông tin học viên
3 Hiển thị danh sách tất cả học viên
4 Hiển thị danh sách học viên thi đỗ (Điểm trung bình >= 75)
5 Hiển thị danh sách học viên thi trượt (Điểm trung bình < 75)
6 Xóa thông tin của học viên
7 Thoát chương trình''')


def get_choice():
    return input("Lựa chọn của bạn ")

def show_list_students():
    print(f"{'mã số':<10}{'Họ Và Tên':^15}{'Giới tính':^15}{'Tỉnh/Thành phố':^15}{'Điểm lý thuyết':^20}{'Điểm thực hành':^10}")
    lst = list_students.split("\n")
    for std in lst:
        if std == "":
            continue
        info = std.split(",")
        id = info[0]
        fullname = info[1]
        gender = info[2]
        province = info[3]
        theory = info[4]
        practice = info[5]
        print(f'{id:<10}{fullname:^15}{gender:^15}{province:^15}{theory:^20}{practice:^10}')

def add_student(list_students):

    id = input("nhập mã sô học sinh: ")
    fullname = input("nhập họ tên: ")
    gender = input("nhập giới tính: ")
    province = input("nhập tỉnh/thành phố: ")
    theory = input ("nhập điểm lý thuyết: ")
    practice = input("nhập điểm thực hành: ")
    list_students += f'\n{id},{fullname},{gender},{province},{theory},{practice}'
    return list_students
def edit_student(list_students): # sửa thông tin học viên
    edit_id = input("nhập vào mã số bạn muốn sửa: ")
    lst = list_students.split("\n")
    new_list_students = ""
    for std in lst:
        info = std.split(",")
        id = info[0]
        if id == edit_id:
            info[0] = input("nhập mã số: ")
            info[1] = input("nhập họ tên: ")
            info[2] = input("nhập giới tính: ")
            info[3] = input("nhập tỉnh/thành phố: ")
            info[4] = input("nhập điểm lý thuyết: ")
            info[5] = input("nhập điểm thực hành: ")


            new_list_students += std + "\n"
    return new_list_students
def show_passed_students():
    print(f"{'mã số':<10}{'Họ Và Tên':^15}{'Giới tính':^15}{'Tỉnh/Thành phố':^15}{'Điểm lý thuyết':^20}{'Điểm thực hành':^10}")
    lst = list_students.split("\n")
    for std in lst:
        if std == "":
            continue
        info = std.split(",")
        id = info[0]
        fullname = info[1]
        gender = info[2]
        province = info[3]
        theory = info[4]
        practice = info[5]
        avg = (int(theory) + int(practice))//2
        if avg >= 75:
            print(f'{id:<10}{fullname:^15}{gender:^15}{province:^15}{theory:^20}{practice:^10}')

def show_failed_student():
    print(
        f"{'mã số':<10}{'Họ Và Tên':^15}{'Giới tính':^15}{'Tỉnh/Thành phố':^15}{'Điểm lý thuyết':^20}{'Điểm thực hành':^10}")
    lst = list_students.split("\n")
    for std in lst:
        if std=="":
            continue
        info = std.split(",")
        id = info[0]
        fullname = info[1]
        gender = info[2]
        province = info[3]
        theory = info[4]
        practice = info[5]
        avg = (int(theory) + int(practice)) // 2
        if avg < 75:
            print(f'{id:<10}{fullname:^15}{gender:^15}{province:^15}{theory:^20}{practice:^10}')

def delete_student(list_students):
    delete_id = input("nhập vào mã số bạn muốn xóa: ")
    lst = list_students.split("\n")
    new_list_students = ""
    for std in lst:
        info = std.split(",")
        id = info[0]
        if id != delete_id:
            new_list_students += std + "\n"
    return new_list_students




while True:
    show_menu()
    user_choice = get_choice()
    if user_choice == "1":
        list_students = add_student(list_students)
    elif user_choice == "2":
        list_students = edit_student(list_students)
    elif user_choice == "3":
        show_list_students()
    elif user_choice == "4":
        show_passed_students()
    elif user_choice == "5":
        show_failed_student()
    elif user_choice == "6":
        new_list_students = delete_student(list_students)
    elif user_choice == "7":
        print("thóat chương trình")
        break


