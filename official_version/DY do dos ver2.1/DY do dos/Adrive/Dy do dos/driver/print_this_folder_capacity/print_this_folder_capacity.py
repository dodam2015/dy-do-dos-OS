import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

# 현재 스크립트가 위치한 디렉토리 경로
script_directory = os.path.dirname(os.path.abspath(__file__))

# 스크립트가 있는 폴더의 용량 계산
folder_size = get_folder_size(script_directory)

# 바이트 단위로 표시
folder_size_mb = folder_size / (1024 * 1024)
folder_size_kb = folder_size / 1024

# 용량 표시
if folder_size_mb <= 0:
    print(f"capacity: {folder_size_mb:.2f} MB")
elif folder_size_kb >= 0.99:
    print(f"capacity: {folder_size_kb:.2f} KB")
else:
    print(f"capacity: {folder_size} Byte")
