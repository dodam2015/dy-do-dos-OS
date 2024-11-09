import os

# 텍스트 파일 이름
file_name = "new_file.txt"

# 현재 스크립트가 위치한 디렉토리의 부모 디렉토리 경로
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 텍스트 파일 경로
file_path = os.path.join(parent_directory, file_name)

# 텍스트 파일 생성 및 내용 작성
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("test file.")

print(f"maked")
