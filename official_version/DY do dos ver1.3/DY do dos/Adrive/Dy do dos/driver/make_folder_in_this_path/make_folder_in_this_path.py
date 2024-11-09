import os

# 새 폴더 이름
new_folder_name = "new_folder"

# 현재 스크립트가 위치한 디렉토리 경로
script_directory = os.path.dirname(os.path.abspath(__file__))

# 새 폴더 경로
new_folder_path = os.path.join(script_directory, new_folder_name)

# 폴더 생성
os.makedirs(new_folder_path, exist_ok=True)

print(f"maked")
