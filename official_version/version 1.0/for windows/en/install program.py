print('loading...')


import time
import os
import shutil
print('Welcome to the dy do dos installer!')
time.sleep(1)
print("install language is 'english'.")
time.sleep(1)
print("start installing")
time.sleep(1)
# 현재 코드가 있는 폴더 경로 (현재 작업 디렉토리)
current_folder = os.path.dirname(os.path.abspath(__file__))

# 복사할 폴더 경로
source_folder = os.path.join(current_folder, "install_program_file", "dy_do_dos_official_1.0")

# 바탕화면 경로 (Windows 환경)
desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")

# 복사될 경로
destination_folder = os.path.join(desktop_folder, "dy_do_dos_official_1.0")

# 폴더를 복사하는 함수
def copy_folder(source, destination):
    try:
        # 만약 destination 폴더가 이미 존재하면 삭제
        if os.path.exists(destination):
            shutil.rmtree(destination)
            print(f"Existing folder deleted: {destination}")

        # 폴더 복사
        shutil.copytree(source, destination)
        print(f"Folder copied successfully: {destination}")
    except shutil.Error as e:
        print(f"Error copying folder: {e}")
    except OSError as e:
        print(f"Failed to copy folder: {e}")

# 폴더 복사 실행
copy_folder(source_folder, destination_folder)

print('File copy completed.')
time.sleep(1)
print('Personalize it')
time.sleep(1)
def mask_korean_input(prompt):
    user_input = input(prompt)
    masked_input = ''.join(['' if '가' <= char <= '힣' else char for char in user_input])
    return masked_input

# 사용 예시
result = mask_korean_input("Please enter your nickname. (No Korean words, change to user if possible): ")
if result=='':
    result='user'
    print("The user's NickNap input is complete.")
else:
    print("The user's NickNap input is complete.")
# 바탕화면 경로 (Windows 환경)
desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")

# nickname.txt 파일 경로
nickname_file = os.path.join(desktop_folder, "dy_do_dos_official_1.0", "user", "nickname.txt")

# 새로운 내용을 정의
new_content = result

# 파일 내용을 변경하는 함수
def change_file_content(file_path, content):
    try:
        # 쓰기 모드로 파일 열기 (기존 내용 덮어쓰기)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File contents changed successfully: {file_path}")
    except Exception as e:
        print(f"Error changing file: {e}")

# 파일 내용 변경 실행
change_file_content(nickname_file, new_content)
time.sleep(1)
print ('Installation is complete. You can now turn off the program.')
print ('Now double-click the official_verison1_0.py file')
time.sleep(10)
quit()