disk_in_thisPC=['X:/']
diskXname='boot_drive'
diskXfull=100000 #mb #100gb
diskXleft=100000 #mb

diskCname='dy do os local drive'
diskXleft-=100
diskCfull=1000 #mb
diskCleft=900 #mb
disk_in_thisPC+=['C:/']

print(f'disk Cdrive (name {diskCname}) {diskCfull}mb / {diskCleft}mb is slected.')

disk_info = {
    'C:/': {'name': diskCname,'full': diskCfull, 'left': diskCleft},
}

system_test_cmd_list=[]

PCname=input('enter your PCname:')

print('importing...')
import time
import tkinter as tk
from tkinter import messagebox
print('loading dy do OS...')
CMDhelp=["index(CMD/help) = help of cmd.", "index(shutdown/help) = see help for shutdown menu.", "disk left = print disk left (input) drive",
         "log-out = log out this user.", "system file fix = change system file",
         "print(enter/variable) = enter variable and you enterd, print variable you entered."]
OSname='dy do OS'
OSverison='alpha2.2'
print('hello, user')
print("help cmd to 'index(CMD/help)'.")
print("this verison is test verison of 'dy do OS'.")
cmd=''
while cmd!='exit':
    cmd=input('C:/')
    if cmd=='index(CMD/help)':
        print('index of CMD/help')
        print(CMDhelp)
    elif cmd=='index(shutdown/help)':
        print("shutdown computer to 'shutdown -s -c'.")
    elif cmd=='shutdown -s -c':
        print('dy do OS is shutdowning...')
        cmd='exit'
    elif cmd=='disk left':
        print(disk_in_thisPC)
        find_disk_left = input("enter drive:")
        if find_disk_left in disk_info:
            print(f'index of {find_disk_left} full/left')
            print(f'name: {disk_info[find_disk_left]["name"]}, {disk_info[find_disk_left]["full"]}mb / {disk_info[find_disk_left]["left"]}mb left.')
        else:
            print(f'no drive {find_disk_left} is not in the PC.')
    elif cmd=='log-out':
        print('log-outing...')
        print("enter 'log-in' or 'shutdown -s -c'.")
        logout_screen_slect=input(':')
        if logout_screen_slect=='log-in':
            print('log-ining...')
        elif logout_screen_slect=='shutdown -s c':
            cmd='exit'
        else:
            print('err.log-out.screen')
    elif cmd=='make(new/developer/disk)':
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
    elif cmd=='system file fix':
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
    elif cmd == 'print(enter/variable)':
        user_input = input("enter variable of system:")
        variables = locals()
        if user_input in variables:
            value = variables[user_input]
            print(f"variable '{user_input}' index: {value}")
        else:
            print(f"variable '{user_input}'is no in the system.")
    elif cmd=='system(test)':
        print('open "system(test)"? (y , n)')
        enter_system_test=input(':')
        if enter_system_test=='y':
            system_test_cmd_list=['color(color_variable)']
            system_test_cmd=''
            while system_test_cmd!='exit':
                print('index of test command:')
                len_sys_test_list=len(system_test_cmd_list)
                find=0
                while find!=len_sys_test_list:
                    print(system_test_cmd_list[find])
                    find+=1
                system_test_cmd=input(':')
                if system_test_cmd=='color A':
                    print('test:err color')
        elif enter_system_test=='n':
            print()
        else:
            print('enter y or n in this slect screen (err.sys.test.yorn.selnot)')
    elif cmd=='system(code)':
        code_make=''
        code_list=[]
        print('enter code, play code command is "play;"and exit is "exit;".')
        while code_make!='exit;' or code_make!='play;':
            code_make=input(':')
            code_list+=code_make
        if code_make=='exit;':
            code_list=[]
            print()
        elif code_make=='play;':
            print('code_list')
quit()