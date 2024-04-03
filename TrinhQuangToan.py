# đọc một file văn bản thành nhiều dòng
# Ghi ra màn hình theo  thứ tự ngược lại của chungs

def reverse_display(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("Không tìm thấy tệp.")

file_path = 'C:\\Users\\Admin\\Desktop\\bailam\\Test.txt'
reverse_display(file_path)
  
#hello trinh quang toan 20A10010263