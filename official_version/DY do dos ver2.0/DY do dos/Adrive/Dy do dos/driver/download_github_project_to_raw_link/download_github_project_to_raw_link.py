import os
import pathlib
import time
import requests            

# 현재 스크립트가 위치한 디렉토리 경로
script_directory = os.path.dirname(os.path.abspath(__file__))
project_folder = os.path.join(script_directory, "user", "admin", "app")

# 저장할 폴더가 없으면 생성
if not os.path.exists(project_folder):
    os.makedirs(project_folder)

print('enter github raw link.')
print('')
file_url = input(':')

# 파일 다운로드
response = requests.get(file_url)
if response.status_code == 200:
    # 파일 이름 추출
    file_name = file_url.split("/")[-1]
    file_path = os.path.join(project_folder, file_name)            
    
    # 파일 저장
    with open(file_path, 'wb') as file:
        file.write(response.content)            
        print('OK')
        time.sleep(1)
        print('download OK.')
else:
    print("error:", response.status_code)
    time.sleep(5)
