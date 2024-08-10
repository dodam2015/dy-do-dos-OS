verison='beta2.0'
disk_in_thisPC=['X:/']
diskXname='boot_drive'
diskXfull=100000 #mb #100gb
diskXleft=100000 #mb
start=0
start=1
if start==1:
    diskCname='dy do os local drive'
    diskXleft-=100
    diskCfull=1000 #mb
    diskCleft=900 #mb
    disk_in_thisPC+=['C:/']

    disk_info = {
        'C:/': {'name': diskCname,'full': diskCfull, 'left': diskCleft},
    }

    print(f'disk Cdrive (name {diskCname}) {diskCfull}mb / {diskCleft}mb is slected.')

    language_this_verison=['korean', 'english']
    print('enter language (korean , english)')
    input_language=input(':')
    if input_language=='korean':
        language='korean'
    elif input_language=='english':
        language='english'
    else:
        language='english'
        print('language set to english')

    if language=='english':
        print('hello, user')
    elif language=='korean':
        print('user님 안녕하세요')
    print('importing...')
    import time
    if language=='english':
        print('loading dy do OS...')
    elif language=='korean':
        print('dy do os 로딩중...')

    CMDhelp=["index(CMD/help) = help of cmd.", "index(shutdown/help) = see help for shutdown menu.", "disk left = print disk left (input) drive",
            "log-out = log out this user.", "system file fix = change system file",
            "print(enter/variable) = enter variable and you enterd, print variable you entered.", "set:language = enter new language",
            "calculator = enter calculator", "dir C:/ = print dir of C:/", "dir(enter) = print dir enter path"]

    OSname='dy do OS'
    OSverison='alpha2.2'

    if language=='english':
        print('welcome!')
        print("help cmd to 'index(CMD/help)'.")
        print("this verison is test verison of 'dy do OS'.")
    elif language=='korean':
        print('환영합니다!')
        print("도움말 명령어는 'index(CMD/help)'.")
        print("이 버전은 'dy do os'의 테스트 버전입니다.")

    cmd=''
    while cmd!='exit':
        cmd=input('C:/')
        if cmd=='index(CMD/help)':
            if language=='english':
                print('index of CMD/help')
                print(CMDhelp)
            elif language=='korean':
                print('CMD/help의 인덱스')
                print(CMDhelp)
        elif cmd=='index(shutdown/help)':
            if language=='english':
                print("shutdown computer to 'shutdown -s -c'.")
            elif language=='korean':
                print("컴퓨터 종료 명령어는 'shutdown -s -c'입니다.")
        elif cmd=='shutdown -s -c':
            if language=='english':
                print('dy do OS is shutdowning...')
                cmd='exit'
            elif language=='korean':
                print('dy do OS가 종료중 입니다...')
                cmd='exit'
        elif cmd=='disk left':
            if language=='english':
                print(disk_in_thisPC)
                find_disk_left = input("enter drive:")
                if find_disk_left in disk_info:
                    print(f'index of {find_disk_left} full/left')
                    print(f'name: {disk_info[find_disk_left]["name"]}, {disk_info[find_disk_left]["full"]}mb / {disk_info[find_disk_left]["left"]}mb left.')
                else:
                    print(f'no drive {find_disk_left} is not in the PC.')
            elif language=='korean':
                    print(disk_in_thisPC)
                    find_disk_left = input("드라이브를 입력하세요:")
                    if find_disk_left in disk_info:
                        print(f'{find_disk_left}의 전체/남음 인덱스')
                        print(f'이름: {disk_info[find_disk_left]["name"]}, {disk_info[find_disk_left]["full"]}mb / {disk_info[find_disk_left]["left"]}mb 가 남았습니다.')
                    else:
                        print(f'드라이브 {find_disk_left}는 이 PC에 존재하지 않습니다.')
        elif cmd=='log-out':
            if language=='english':
                print('log-outing...')
                print("enter 'log-in' or 'shutdown -s -c'.")
                logout_screen_slect=input(':')
                if logout_screen_slect=='log-in':
                    print('log-ining...')
                elif logout_screen_slect=='shutdown -s c':
                    cmd='exit'
                else:
                    print('err.log-out.screen')
            elif language=='korean':
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
            if language=='english':
                if diskXleft >= 1000:
                    print('enter new developer disk label ex(E:/)')
                    user_disk = input(':')
                    user_disk_name = input('enter disk name:')
                    user_disk_full = int(input('enter new developer disk full mb:'))
                    if user_disk_full >= diskXfull - 1000:
                        print("You're trying to make more disks than your computer has.")
                        user_disk = ''
                        user_disk_name = ''
                        user_disk_full = 0
                    else:
                        diskXfull -= user_disk_full
                        user_disk_left = user_disk_full - 1
                        disk_info[user_disk] = {"name": user_disk_name, "full": user_disk_full, "left": user_disk_left}  # mb
                        disk_in_thisPC.append(user_disk)  # 리스트에 추가
                else:
                    print('diskXboot drive storage is 1GB now. stop make the drive.')
            elif language=='korean':
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
            if language=='english':
                slect_sys_file_fix=input('real? (y,n):')
                if slect_sys_file_fix=='y':
                    print('loading system file fix program...')
                    print('slect system file settings')
                    sys_file_fix_cmd=0
                    while sys_file_fix_cmd!='exit':
                        print('1.disk_in_thisPC')
                        print('exit')
                        sys_file_fix_cmd=input(':')
                        if sys_file_fix_cmd=='disk_in_thisPC':
                            print('input disk_in_thisPC new list item')
                            sys_file_fix_disk_in_thisPC=input(':')
                            disk_in_thisPC+=[sys_file_fix_disk_in_thisPC]
                        elif sys_file_fix_cmd=='exit':
                            print('')
                        else:
                            print('sys.file.fix.command.not')
                elif slect_sys_file_fix=='n':
                    print('OK.')
                else:
                    print('err.sys.file.fix.program.slect.yorn')
            elif language=='korean':
                slect_sys_file_fix=input('진짜요? (y,n):')
                if slect_sys_file_fix=='y':
                    print('시스템 파일를 고치는 프로그램을 로딩중...')
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
                    print('OK.')
                else:
                    print('err.sys.file.fix.program.slect.yorn')
        elif cmd == 'print(enter/variable)':
            if language=='english':
                user_input = input("enter variable of system:")
                variables = locals()
                if user_input in variables:
                    value = variables[user_input]
                    print(f"variable '{user_input}' index: {value}")
                else:
                    print(f"variable '{user_input}'is no in the system.")
            elif language=='korean':
                user_input = input("시스템 변수를 입력하세요:")
                variables = locals()
                if user_input in variables:
                    value = variables[user_input]
                    print(f"변수 '{user_input}'의 인덱스는: {value}")
                else:
                    print(f"변수 '{user_input}'는 시스템에 존재하지 않습니다.")
        elif cmd=='set:language':
            if language=='english':
                print(language_this_verison)
                slect_language=input('input new language:')
                if slect_language in language_this_verison:
                    language=slect_language
                else:
                    print('error no language in this verison.')
            elif language=='korean':
                print(language_this_verison)
                slect_language=input('새로운 언어를 입력하세요:')
                if slect_language in language_this_verison:
                    language=slect_language
                else:
                    print('에러: 당신이 입력한 언어는 존재하지 않습니다.')
        elif cmd=='calculator':
            if language=='english':
                print('choose one in + - * /')
                calcul_math_enter = input(':')
                try:
                    if calcul_math_enter == '+':
                        print("enter like n+n ('n' is number)")
                        a, b = map(int, input('').split('+'))
                        calcul_math_answer = a + b
                        print(calcul_math_answer)
                    elif calcul_math_enter == '-':
                        print("enter like n-n ('n' is number)")
                        a, b = map(int, input('').split('-'))
                        calcul_math_answer = a - b
                        print(calcul_math_answer)
                    elif calcul_math_enter == '*':
                        print("enter like n*n ('n' is number)")
                        a, b = map(int, input('').split('*'))
                        calcul_math_answer = a * b
                        print(calcul_math_answer)
                    elif calcul_math_enter == '/':
                        print("enter like n/n ('n' is number)")
                        a, b = map(int, input('').split('/'))
                        calcul_math_answer = a / b  # 나누기 연산 수정
                        print(calcul_math_answer)
                    else:
                        print('err.calculator')
                except ValueError:
                    print('enter error: enter number')
                except ZeroDivisionError:
                    print('error: It cannot be divided by zero.')
                except Exception as e:
                    print(f'error: {e}')
            elif language=='korean':
                print('choose one in + - * /')
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
else:
    print('???err.not.found???')