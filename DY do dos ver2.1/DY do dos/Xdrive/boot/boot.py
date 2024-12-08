cd=0
vd=''
import time
import os


#[
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

# 현재 스크립트가 위치한 디렉토리의 부모 디렉토리 경로
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 부모 폴더의 용량 계산
folder_size = get_folder_size(parent_directory)

# 바이트 단위로 표시
folder_size_mb = folder_size / (1024 * 1024)
folder_size_kb = folder_size / 1024

if folder_size_kb>=5.00:
    quit()    

#]


version='PCset.boot'

#[
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

# 현재 스크립트가 위치한 디렉토리의 부모 디렉토리 경로
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 부모 폴더의 용량 계산
folder_size = get_folder_size(parent_directory)

# 바이트 단위로 표시
folder_size_mb = folder_size / (1024 * 1024)
folder_size_kb = folder_size / 1024

# 용량 표시
if folder_size_mb <= 0:
    print(f"load X drive {folder_size_mb:.2f}MB/5kb")
elif folder_size_kb >= 0.99:
    print(f"load X drive {folder_size_kb:.2f}KB/5kb")
else:
    print(f"load X drive {folder_size}Byte/5kb")
#]
time.sleep(1)

work=''
while work!='exit':
    print('select work:')
    print('1.exit')
    print('')
    work=int(input(':'))
    if work==1 or work=='exit':
        quit()