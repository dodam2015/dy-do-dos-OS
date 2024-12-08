import requests
from bs4 import BeautifulSoup
import os

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

    # 현재 스크립트의 부모 폴더의 부모 폴더 경로 가져오기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))

    # 결과를 developer.py 파일에 저장할 경로
    file_path = os.path.join(parent_parent_dir, 'developer.py')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(f"웹사이트 내용이 {file_path} 파일에 저장되었습니다.")
else:
    print(f"웹사이트 접근 실패: {response.status_code}")
