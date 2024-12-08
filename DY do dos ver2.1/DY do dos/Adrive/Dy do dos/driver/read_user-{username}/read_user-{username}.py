import os
# 현재 스크립트가 위치한 디렉토리 경로
script_directory = os.path.dirname(os.path.abspath(__file__))
user_directory = os.path.join(script_directory, "user")

# user 디렉토리 내의 폴더 읽기
if os.path.exists(user_directory):
    folders = [folder for folder in os.listdir(user_directory) if os.path.isdir(os.path.join(user_directory, folder))]

    print(folders)
else:
    print("error")