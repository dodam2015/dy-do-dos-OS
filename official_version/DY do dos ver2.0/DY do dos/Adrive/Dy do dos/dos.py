import time
import os
import requests
import subprocess
import pygame
from bs4 import BeautifulSoup
import ctypes
import sys

os_version='official_2.0'
os_name='Dy do dos'
os_versionv=os_version[9:12]
disk_inf=['A:/', 'X:/']


if 1==0:
    # 초기화
    pygame.mixer.init()

    # 현재 스크립트가 위치한 디렉토리 경로
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # MP3 파일 경로 설정
    file_path = os.path.join(script_directory,"systemfile", "startup.mp3")

    # 음악 파일 재생
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


time.sleep(5)


# 현재 스크립트가 위치한 디렉토리 경로
script_directory = os.path.dirname(os.path.abspath(__file__))

# 부모 폴더의 부모 폴더 경로
parent_directory = os.path.dirname(os.path.dirname(script_directory))

# 부모 폴더의 이름 추출
parent_name = os.path.basename(parent_directory)

# 이름 확인
if parent_name != 'DY do dos':
    print('error')
    quit()


print()
print()
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
    print(f"load A drive {folder_size_mb:.2f}MB/100mb")
elif folder_size_kb >= 0.99:
    print(f"load A drive {folder_size_kb:.2f}KB/100mb")
else:
    print(f"load A drive {folder_size}Byte/100mb")
#]

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

if folder_size_mb>=100.00:
    quit()    
#]



print('continue to wait 3s')
time.sleep(3)

print('DY do dos is loading...')

# 현재 스크립트가 위치한 디렉토리 경로
script_directory = os.path.dirname(os.path.abspath(__file__))
user_directory = os.path.join(script_directory, "user")

# user 디렉토리 내의 폴더 읽기
if os.path.exists(user_directory):
    folders = [folder for folder in os.listdir(user_directory) if os.path.isdir(os.path.join(user_directory, folder))]
else:
    print("error")

user_name=folders

print()
print('loaded')
print()
print(f'welcome, {str(folders)}')
print()
cmd=0
while cmd!='shutdown -s -lo- -li-'or cmd!='exit':
    cmd=input('A:/')
    if cmd=='get Adrive capacity;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]


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
            print(f"load A drive {folder_size_mb:.2f}MB/100mb")
        elif folder_size_kb >= 0.99:
            print(f"load A drive {folder_size_kb:.2f}KB/100mb")
        else:
            print(f"load A drive {folder_size}Byte/100mb")
        #]

    elif cmd=='get github rawlink*download;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]
        print('loading github system...')
        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))
        project_folder = os.path.join(script_directory, "user", "admin", "app")
        # 저장할 폴더가 없으면 생성
        if not os.path.exists(project_folder):
            os.makedirs(project_folder)
        print('enter github raw link.')
        print('help to {none}')
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
    elif cmd=='run python app;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]
        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))
        app_directory = os.path.join(script_directory, "user", "admin", "app")

        # 사용자로부터 파일 이름 입력 받기
        file_name = input("enter app name (don't enter .py) :")
        print()
        # 파일 경로 생성
        file_path = os.path.join(app_directory, f"{file_name}.py")

        # 파일이 존재하는지 확인하고 실행
        if os.path.exists(file_path):
            subprocess.run(["python3", file_path])  # Python 3.x를 사용하고 있다면 'python' 대신 'python3'를 사용할 수 있습니다.
        else:
            print(f"error: {file_name}.py")
    elif cmd=='get dir app;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]
        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))
        app_directory = os.path.join(script_directory, "user", "admin", "app")

        # app 디렉토리 내의 모든 파일 읽기
        if os.path.exists(app_directory):
            files = [file for file in os.listdir(app_directory) if os.path.isfile(os.path.join(app_directory, file))]
    
            print("dir of user/admin/app:")
            for file in files:
               print('  '+file)
        else:
            print("error not.founded.folder")
    elif cmd=='help' or cmd=='get help;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]
        print('index of cmd/help')
        print(' get Adrive capacity;')
        print(' get github rawlink*download;')
        print(' run python app;')
        print(' get dir app;')
        print(' print enter variable;')
        print(' get os version;')
        print(' make folder in desktop;')
        print(' get dir desktop;')
        print(' make text_file in desktop;')
        print(' shutdown;')
        print(' version check;')
        print(' developer version:')
    elif cmd=='print enter variable;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]

        user_input = input("enter system variable:")
        variables = locals()
        if user_input in variables:
            value = variables[user_input]
            print(f"the value of {user_input} is '{value}'.")
        else:
            print(f"variable '{user_input}'is none.")
    elif cmd=='get os version;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]
        print('os name:')
        print(os_name)
        print('os version:')
        print(os_version)
    elif cmd=='make folder in desktop;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]

        folder_name = input('enter folder name:')
        # 새 폴더 이름
        new_folder_name = f"user/admin/desktop/{folder_name}"

        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # 새 폴더 경로
        new_folder_path = os.path.join(script_directory, new_folder_name)

        # 폴더 생성
        os.makedirs(new_folder_path, exist_ok=True)

        print(f"maked")

    elif cmd=='get dir desktop;':
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

        if folder_size_mb>=100.00:
            quit()    
        #]
        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))
        app_directory = os.path.join(script_directory, "user", "admin", "desktop")

        # app 디렉토리 내의 모든 파일 및 폴더 읽기
        if os.path.exists(app_directory):
            items = os.listdir(app_directory)  # 파일과 폴더 목록 가져오기

            print("dir of user/admin/desktop:")
            for item in items:
                item_path = os.path.join(app_directory, item)  # 각 항목의 전체 경로
                print('  ' + item)

                # 파일인 경우 내용 출력
                if os.path.isfile(item_path):
                    with open(item_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        print(' --', content)
                        print()  # 추가적인 줄 바꿈
        else:
            print("error: folder not found")
    elif cmd=='make text_file in desktop;':
        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))
        app_directory = os.path.join(script_directory, "user", "admin", "desktop")

        # 디렉토리가 존재하는지 확인
        if not os.path.exists(app_directory):
            os.makedirs(app_directory)  # 디렉토리가 없으면 생성
        
        name=input('enter file name:')
        # 생성할 텍스트 파일 경로
        file_path = os.path.join(app_directory, f"{name}")
        
        text=input('enter text:')
        # 텍스트 파일 생성 및 내용 작성
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

        print(f"file maked")
    elif cmd=='shutdown;':
        print('shutdowning this dos...')
        time.sleep(1)
        quit()
    elif cmd=='version check;':
        url = "https://tangerine-pasca-fe88b3.netlify.app/"
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            for title in soup.find_all('title'):
                title.decompose()
            page_text = soup.get_text(separator=" ")  # 공백으로 구분
            temp11=page_text.strip()
            print(temp11)  # 양쪽 공백 제거 후 출력
            if os_versionv==temp11:
                print('this DY do dos version is latest version')
            elif os_versionv<temp11:
                print(f'latest version=={temp11} update Dy do dos')
            elif os_versionv>temp11:
                print('this DY do dos version is developer version')
    elif cmd=='developer version:;':
        print('loading')
        time.sleep(1)
        print('1.developer version1 ')
        t=int(input('enter number:'))
        if t==1:
            # 웹사이트 URL
            url = 'https://dydodosdevelopercodepage.netlify.app/'

            # 웹사이트 내용 가져오기
            response = requests.get(url)

            # 응답이 성공적이면
            if response.status_code == 200:
                # HTML 내용 파싱
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 제목 태그 삭제
                for title in soup.find_all('title'):
                    title.decompose()  # 제목 태그 삭제

                # 전체 텍스트 가져오기 (제목 제외)
                text = soup.get_text()

                # 공백 제거 (줄바꿈은 유지)
                cleaned_text = '\n'.join(line for line in text.splitlines() if line.strip())

                # 현재 스크립트의 경로 가져오기
                current_dir = os.path.dirname(os.path.abspath(__file__))
                
                # 결과를 developer.py 파일에 저장 (현재 스크립트 폴더에)
                file_path = os.path.join(current_dir, 'developer.py')
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(cleaned_text)
                # developer.py 파일 실행
                subprocess.run(['python', file_path])
            else:
                print(f"error: {response.status_code}")
