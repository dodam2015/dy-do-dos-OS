import os
import subprocess
import requests
import time
from pathlib import Path
version='official_1.2'
disk_in_thisPC=['X:/']
diskXname='boot_drive'
diskXfull=100000 #mb #100gb
diskXleft=100000 #mb

desktop_path = Path.home() / 'Desktop'
folder_path = desktop_path / f'dy_do_dos_{version}'
if os.path.exists(folder_path):
    desktop_path = Path.home() / 'Desktop'
    folder_path = desktop_path / f'dy_do_dos_{version}'
    installed_file_path = folder_path / 'installed.txt'
    # 파일 존재 여부 및 내용 확인
    if os.path.exists(installed_file_path):
        with open(installed_file_path, 'r') as file:
            content = file.read().strip()
            if content == '1':
                installed=1
            else:
                installed=0
    else:
        installed=0
else:
    installed = 0

if installed==0:
    print('install dy do dos. [err.drive.a.not.found]')
elif installed==1:
    diskCname='dy do os 로컬 디스크'
    diskXleft-=100
    diskCfull=1000 #mb
    diskCleft=900 #mb
    disk_in_thisPC+=['A:/']
    disk_info = {
        'A:/': {'name': diskCname,'full': diskCfull, 'left': diskCleft},
    }
    print(f'disk Adrive (name {diskCname}) {diskCfull}mb / {diskCleft}mb is slected.')

    desktop_path = Path.home() / 'Desktop'
    nickname_file_path = desktop_path / f'dy_do_dos_{version}' / 'user' / 'nickname.txt'
    if os.path.exists(nickname_file_path):
        with open(nickname_file_path, 'r') as file:
            content = file.read().strip()
            print(f"안녕하세요! {content}님.")
    else:
        print('err.nickname.not.found')
        pass
    
    print('importing...')
    import time
    print('dy do os 로딩중...')
    CMDhelp=["index(CMD/help) = 명령창의 도움말.", "index(shutdown/help) = 전원 메뉴의 도움말.", "disk left = 디스크의 용량 남음을 표시하는 명령어.",
            "log-out = 사용자를 로그아웃 시킵니다.", "system file fix = 시스템 파일을 수정할 수 있는 명령어.",
            "print(enter/variable) = 사용자가 입력한 변수의 값을 출력합니다."
            "calculator = 계산기를 실행 시킵니다.", "dir A:/ = A:/의 디렉토리를 출력합니다.", "dir(enter) = 사용자가 입력한 경로의 디렉토리를 출력합니다.",
            "store = 스토어를 엽니다.", "oepn(app/enter) = 사용자가 입력한 경로의 파일을 실행합니다."]
    
    OSname='dy do OS'

    print('환영합니다!')
    print("도움말 명령어는 'index(CMD/help)'를 치세요.")
    print("이 버전은 'dy do os'의 정식 버전입니다.")

    cmd=''
    while cmd!='exit':
        cmd=input('A:/')
        if cmd=='index(CMD/help)':
            print('CMD/help의 인덱스')
            print(CMDhelp)
        elif cmd=='index(shutdown/help)':
            print("컴퓨터 종료 명령어는 'shutdown -s -c'입니다.")
        elif cmd=='shutdown -s -c':
            print('dy do OS가 종료중 입니다...')
            cmd='exit'
        elif cmd=='disk left':
            print(disk_in_thisPC)
            find_disk_left = input("드라이브를 입력하세요:")
            if find_disk_left in disk_info:
                print(f'{find_disk_left}의 전체/남음 인덱스')
                print(f'이름: {disk_info[find_disk_left]["name"]}, {disk_info[find_disk_left]["full"]}mb / {disk_info[find_disk_left]["left"]}mb 가 남았습니다.')
            else:
                print(f'드라이브 {find_disk_left}는 이 PC에 존재하지 않습니다.')
        elif cmd=='log-out':
            print('로그 아웃중...')
            print("'log-in' 또는 'shutdown -s -c'를 입력하세요.")
            logout_screen_slect=input(':')
            if logout_screen_slect=='log-in':
                print('로그인 중...')
            elif logout_screen_slect=='shutdown -s c':
                cmd='exit'
            else:
                print('err.log-out.screen')

        elif cmd=='make(new/developer/disk)':
            if diskXleft >= 1000:
                print('새로운 개발자 디스크 라벨을 입력하세요 예(E:/)')
                user_disk = input(':')
                user_disk_name = input('디스크 이름을 입력하세요:')
                user_disk_full = int(input('개발자 디스크의 전체 mb를 입력하세요:'))
                if user_disk_full >= diskXfull - 1000:
                    print("당신은 이 컴퓨터가 가지고 있는 용량보다 더 많은 용량을 선택했습니다.")
                    user_disk = ''
                    user_disk_name = ''
                    user_disk_full = 0
                else:
                    diskXfull -= user_disk_full
                    user_disk_left = user_disk_full - 1
                    disk_info[user_disk] = {"name": user_disk_name, "full": user_disk_full, "left": user_disk_left}  # mb
                    disk_in_thisPC.append(user_disk)  # 리스트에 추가
            else:
                print('boot drive X가 이제 1gb만 남았습니다. 그만 만드세요.')
        elif cmd=='system file fix':
            slect_sys_file_fix=input('실행할까요? (y,n):')
            if slect_sys_file_fix=='y':
                print('시스템 파일을 수정하는 앱 로딩중...')
                print('시스템 파일 설정을 선택하세요')
                sys_file_fix_cmd=0
                while sys_file_fix_cmd!='exit':
                    print('1.disk_in_thisPC')
                    print('exit')
                    sys_file_fix_cmd=input(':')
                    if sys_file_fix_cmd=='disk_in_thisPC':
                        print('disk_in_thisPC의 새로운 항목을 입력하세요')
                        sys_file_fix_disk_in_thisPC=input(':')
                        disk_in_thisPC+=[sys_file_fix_disk_in_thisPC]
                    elif sys_file_fix_cmd=='exit':
                        print('')
                    else:
                        print('sys.file.fix.command.not')
            elif slect_sys_file_fix=='n':
                print('네')
            else:
                print('err.sys.file.fix.program.slect.yorn')
        elif cmd == 'print(enter/variable)':
            user_input = input("시스템 변수를 입력하세요:")
            variables = locals()
            if user_input in variables:
                value = variables[user_input]
                print(f"변수 '{user_input}'의 값은: {value}입니다.")
            else:
                print(f"변수 '{user_input}'는 시스템에 존재하지 않습니다.")
        elif cmd=='calculator':
            print('+ - * / 에서 하나를 고르세요')
            calcul_math_enter = input(':')
            try:
                if calcul_math_enter == '+':
                    print("n+n같이 입력하세요 ('n은 숫자입니다.')")
                    a, b = map(int, input('').split('+'))
                    calcul_math_answer = a + b
                    print(calcul_math_answer)
                elif calcul_math_enter == '-':
                    print("n-n같이 입력하세요 ('n은 숫자입니다.')")
                    a, b = map(int, input('').split('-'))
                    calcul_math_answer = a - b
                    print(calcul_math_answer)
                elif calcul_math_enter == '*':
                    print("n*n같이 입력하세요 ('n은 숫자입니다.')")
                    a, b = map(int, input('').split('*'))
                    calcul_math_answer = a * b
                    print(calcul_math_answer)
                elif calcul_math_enter == '/':
                    print("n/n같이 입력하세요 ('n은 숫자입니다.')")
                    a, b = map(int, input('').split('/'))
                    calcul_math_answer = a / b  # 나누기 연산 수정
                    print(calcul_math_answer)
                else:
                    print('err.calculator')
            except ValueError:
                print('에러:숫자를 입력하세요.')
            except ZeroDivisionError:
                print('에러:0으로 나눌수 없습니다.')
            except Exception as e:
                print(f'에러: {e}')
        elif cmd=='dir A:/':
            # 바탕화면의 dy_do_dos_beta2.0 경로 설정
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", f"dy_do_dos_{version}")
            # 디렉토리 내용 표시
            try:
                if os.path.isdir(desktop_path):
                    print("'A:/'의 디렉토리 [")
                    for item in os.listdir(desktop_path):
                        item_path = os.path.join(desktop_path, item)
                        if os.path.isdir(item_path):
                            print(f"    {item} (폴더)")
                        else:
                            # 파일의 확장명을 표시
                            file_name, file_extension = os.path.splitext(item)
                            print(f"    {item} (파일: {file_extension})")
                    print(']')
                else:
                    print("에러")
            except Exception as e:
                print(f"에러: {e}")
        elif cmd=='dir(enter)':
            desktop_base_path = os.path.join(os.path.expanduser("~"), "Desktop", f"dy_do_dos_{version}")
            relative_path = input("경로를 입력하세요:")
            if relative_path=='C:/':
                print('C드라이브는 다른 OS가 설치돼어 있습니다.')
            else:
                full_path = os.path.join(desktop_base_path, relative_path)
                try:
                    if os.path.isdir(full_path):
                        print(f"{full_path}의 디렉토리[")
                        for item in os.listdir(full_path):
                            item_path = os.path.join(full_path, item)
                            if os.path.isdir(item_path):
                                print(f"    {item} (폴더)")
                            else:
                                file_name, file_extension = os.path.splitext(item)
                                print(f"    {item} (파일: {file_extension})")
                        print(']')
                    else:
                        print("A:/에 입력 경로가 존재하지 않습니다.")
                except Exception as e:
                    print(f"error: {e}")

        elif cmd=='store':
            print('DY do dos 스토어')
            print('앱을 선택하거나(1) 직접 raw url 입력하기(2)')
            print('둘 중에 선택하세요:')
            a=str(input(':'))
            if a=='1':
                print('앱을 선택하세요')
                print('1.test app')
                app=input('')
                if app=='test app':
                    # 바탕화면 경로와 저장할 폴더 이름
                    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                    project_folder = os.path.join(desktop_path, f'dy_do_dos_{version}', "user","app")

                    # 저장할 폴더가 없으면 생성
                    if not os.path.exists(project_folder):
                        os.makedirs(project_folder)

                    # 다운로드할 GitHub 파일의 원본 URL (raw URL)
                    file_url = "https://raw.githubusercontent.com/dodam2015/dy-do-dos-app-Repository/main/test app/test app.py"  # 여기에 실제 파일의 raw URL 입력

                    # 파일 다운로드
                    response = requests.get(file_url)

                    if response.status_code == 200:
                        # 파일 이름 추출
                        file_name = file_url.split("/")[-1]
                        file_path = os.path.join(project_folder, file_name)
                        
                        # 파일 저장
                        with open(file_path, 'wb') as file:
                            file.write(response.content)
                        
                        print(f"{file_name}이 {project_folder}에 다운로드되었습니다.")
                        time.sleep(1)
                        print('다운로드가 완료되었습니다.')
                    else:
                        print("파일 다운로드 중 오류 발생:", response.status_code)
            if a=='2':
                # 바탕화면 경로와 저장할 폴더 이름
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                project_folder = os.path.join(desktop_path, f'dy_do_dos_{version}', "user","app")
                # 저장할 폴더가 없으면 생성
                if not os.path.exists(project_folder):
                    os.makedirs(project_folder)
                print('raw url를 입력하세요.')
                file_url=input(':')
                # 파일 다운로드
                response = requests.get(file_url)
                if response.status_code == 200:
                    # 파일 이름 추출
                    file_name = file_url.split("/")[-1]
                    file_path = os.path.join(project_folder, file_name)            
                    # 파일 저장
                    with open(file_path, 'wb') as file:
                        file.write(response.content)            
                        print(f"{file_name}이 {project_folder}에 다운로드되었습니다.")
                        time.sleep(1)
                        print('다운로드가 완료되었습니다.')
                else:
                    print("파일 다운로드 중 오류 발생:", response.status_code)
                time.sleep(5)
        elif cmd=='open(app/enter)':
            # 바탕화면의 dy_do_dos_official_1.1 경로 설정
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", f"dy_do_dos_{version}", "user", "app")
            # A:\ 경로에서 사용자 입력 받기
            user_input = input("실행할 파일을 입력하세요 (예: app.py): ")
            # 실제 파일 경로 생성
            file_path = os.path.join(desktop_path, user_input)
            # 파일이 존재하는지 확인
            if os.path.isfile(file_path):
                # 파일 실행
                try:
                    subprocess.run(["python", file_path], check=True)
                    print(f"{user_input} 파일이 실행되었습니다.")
                except subprocess.CalledProcessError as e:
                    print("파일 실행 중 오류 발생:", e)
            else:
                print(f"{user_input} 파일이 존재하지 않습니다.")
                
else:
    print('???err.not.found???')