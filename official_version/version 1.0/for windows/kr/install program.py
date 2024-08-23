print('로딩중...')


import time
import os
import shutil
print('dy do dos 설치 프로그램에 오신것을 환영합니다!')
time.sleep(1)
print("설치할 언어는 '한국어'입니다.")
time.sleep(1)
print("설치를 시작합니다.")
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
            print(f"기존 폴더가 삭제되었습니다: {destination}")

        # 폴더 복사
        shutil.copytree(source, destination)
        print(f"폴더가 성공적으로 복사되었습니다: {destination}")
    except shutil.Error as e:
        print(f"폴더를 복사하는 중 오류가 발생했습니다: {e}")
    except OSError as e:
        print(f"폴더 복사 실패: {e}")

# 폴더 복사 실행
copy_folder(source_folder, destination_folder)

print('파일 복사 완료.')
time.sleep(1)
print('개인 설정을 하세요')
time.sleep(1)
def mask_korean_input(prompt):
    user_input = input(prompt)
    masked_input = ''.join(['' if '가' <= char <= '힣' else char for char in user_input])
    return masked_input

# 사용 예시
result = mask_korean_input("닉네임을 입력하세요. (한글은 안됨, 만약 하게 되면 user로 변경): ")
if result=='':
    result='user'
    print('사용자의 닉네임 입력 완료.')
else:
    print('사용자의 닉네임 입력 완료.')
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
        print(f"파일 내용이 성공적으로 변경되었습니다: {file_path}")
    except Exception as e:
        print(f"파일을 변경하는 중 오류가 발생했습니다: {e}")

# 파일 내용 변경 실행
change_file_content(nickname_file, new_content)
time.sleep(1)
print('설치가 완료되었습니다. 이제 프로그램을 꺼셔도 좋습니다.')
print('이제 official_verison1_0.py파일을 더블클릭 하세요.')
time.sleep(10)
quit()