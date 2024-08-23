import os
from pathlib import Path
version='official_1.0'
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
    diskCname='dy do os local disk'
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
            print(f"welcome! {content}.")
    else:
        print('err.nickname.not.found')
        pass
    
    print('importing...')
    import time
    print('dy do os is loading...')
    CMDhelp=["index(CMD/help) = help of cmd.", "index(shutdown/help) = help of shutdwon.", "disk left = print disk full/left",
            "log-out = log-out user.", "system file fix = this command can fix system file.",
            "print(enter/variable) = enter variable and show enter variable of value."
            "calculator = open calculator app.", "dir A:/ = show directory of 'A:/'drive.", "dir(enter) = enter directory, this app show enter dir."]
    
    OSname='dy do OS'

    print('welocme!')
    print("help command is 'index(CMD/help)'.")
    print("this version is official version of 'dy do os'")

    cmd=''
    while cmd!='exit':
        cmd=input('A:/')
        if cmd=='index(CMD/help)':
            print('index of CMD/help')
            print(CMDhelp)
        elif cmd=='index(shutdown/help)':
            print("shutdown dos command is 'shutdown -s -c'.")
        elif cmd=='shutdown -s -c':
            print('shutdowning dy do OS...')
            cmd='exit'
        elif cmd=='disk left':
            print(disk_in_thisPC)
            find_disk_left = input("enter drive:")
            if find_disk_left in disk_info:
                print(f'full and left of {find_disk_left}')
                print(f'name: {disk_info[find_disk_left]["name"]}, {disk_info[find_disk_left]["full"]}mb / {disk_info[find_disk_left]["left"]}mb left.')
            else:
                print(f'drive {find_disk_left} does not exist on this PC.')
        elif cmd=='log-out':
            print('log-outing...')
            print("enter 'log-in' or 'shutdown -s -c'")
            logout_screen_slect=input(':')
            if logout_screen_slect=='log-in':
                print('log-ining...')
            elif logout_screen_slect=='shutdown -s c':
                cmd='exit'
            else:
                print('err.log-out.screen')

        elif cmd=='make(new/developer/disk)':
            if diskXleft >= 1000:
                print('enter new devloper disk label ex(E:/)')
                user_disk = input(':')
                user_disk_name = input('enter disk name:')
                user_disk_full = int(input('enter developer disk mb:'))
                if user_disk_full >= diskXfull - 1000:
                    print("You have chosen more capacity than this computer has.")
                    user_disk = ''
                    user_disk_name = ''
                    user_disk_full = 0
                else:
                    diskXfull -= user_disk_full
                    user_disk_left = user_disk_full - 1
                    disk_info[user_disk] = {"name": user_disk_name, "full": user_disk_full, "left": user_disk_left}  # mb
                    disk_in_thisPC.append(user_disk)  # 리스트에 추가
            else:
                print('I only have 1gb left of boot drive X. Stop making it.')
        elif cmd=='system file fix':
            slect_sys_file_fix=input('open? (y,n):')
            if slect_sys_file_fix=='y':
                print('system file fix program is loading...')
                print('selct system file fix in list')
                sys_file_fix_cmd=0
                while sys_file_fix_cmd!='exit':
                    print('1.disk_in_thisPC')
                    print('exit')
                    sys_file_fix_cmd=input(':')
                    if sys_file_fix_cmd=='disk_in_thisPC':
                        print('enter new entrt of disk_in_thisPC')
                        sys_file_fix_disk_in_thisPC=input(':')
                        disk_in_thisPC+=[sys_file_fix_disk_in_thisPC]
                    elif sys_file_fix_cmd=='exit':
                        print('')
                    else:
                        print('sys.file.fix.command.not')
            elif slect_sys_file_fix=='n':
                print('yes')
            else:
                print('err.sys.file.fix.program.slect.yorn')
        elif cmd == 'print(enter/variable)':
            user_input = input("enter system variable:")
            variables = locals()
            if user_input in variables:
                value = variables[user_input]
                print(f"variable '{user_input}' value is {value}.")
            else:
                print(f"variable '{user_input}' does not exist on the system.")
        elif cmd=='calculator':
            print('selct in + - * / ')
            calcul_math_enter = input(':')
            try:
                if calcul_math_enter == '+':
                    print("enter like n+n ('n is number.')")
                    a, b = map(int, input('').split('+'))
                    calcul_math_answer = a + b
                    print(calcul_math_answer)
                elif calcul_math_enter == '-':
                    print("enter like n-n ('n is number.')")
                    a, b = map(int, input('').split('-'))
                    calcul_math_answer = a - b
                    print(calcul_math_answer)
                elif calcul_math_enter == '*':
                    print("enter like n*n ('n is number.')")
                    a, b = map(int, input('').split('*'))
                    calcul_math_answer = a * b
                    print(calcul_math_answer)
                elif calcul_math_enter == '/':
                    print("enter like n/n ('n is number.')")
                    a, b = map(int, input('').split('/'))
                    calcul_math_answer = a / b  # 나누기 연산 수정
                    print(calcul_math_answer)
                else:
                    print('err.calculator')
            except ValueError:
                print('error:enter number.')
            except ZeroDivisionError:
                print('error:divide it by zero.')
            except Exception as e:
                print(f'error: {e}')
        elif cmd=='dir A:/':
            # 바탕화면의 dy_do_dos_beta2.0 경로 설정
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", f"dy_do_dos_{version}")
            # 디렉토리 내용 표시
            try:
                if os.path.isdir(desktop_path):
                    print("dir of 'A:/' [")
                    for item in os.listdir(desktop_path):
                        item_path = os.path.join(desktop_path, item)
                        if os.path.isdir(item_path):
                            print(f"    {item} (folder)")
                        else:
                            # 파일의 확장명을 표시
                            file_name, file_extension = os.path.splitext(item)
                            print(f"    {item} (file: {file_extension})")
                    print(']')
                else:
                    print("error")
            except Exception as e:
                print(f"error: {e}")
        elif cmd=='dir(enter)':
            desktop_base_path = os.path.join(os.path.expanduser("~"), "Desktop", f"dy_do_dos_{version}")
            relative_path = input("enter path:")
            if relative_path=='C:/':
                print('drive C has a different OS installed.')
            else:
                full_path = os.path.join(desktop_base_path, relative_path)
                try:
                    if os.path.isdir(full_path):
                        print(f"dir of {full_path}[")
                        for item in os.listdir(full_path):
                            item_path = os.path.join(full_path, item)
                            if os.path.isdir(item_path):
                                print(f"    {item} (folder)")
                            else:
                                file_name, file_extension = os.path.splitext(item)
                                print(f"    {item} (file: {file_extension})")
                        print(']')
                    else:
                        print("A:/ does not have an input path.")
                except Exception as e:
                    print(f"error: {e}")


else:
    print('???err.not.found???')