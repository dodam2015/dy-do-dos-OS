disk_in_thisPC=[]
diskCname='dy do os local drive'
diskCfull=1000 #mb
diskCleft=9000 #mb
disk_in_thisPC+=['C:/']

print(f'disk Cdrive (name {diskCname}) {diskCfull}mb / {diskCleft}mb is slected.')

disk_info = {
    'C:/': {'full': diskCfull, 'left': diskCleft},
}

PCname=input('enter your PCname:')

print('importing...')
import time
import tkinter as tk
from tkinter import messagebox
print('loading dy do OS...')
CMDhelp=["index(CMD/help) = help of cmd.", "index(shutdown/help) = see help for shutdown menu.", "disk left = print disk left (input) drive", "log-out = log out this user.", ""]
OSname='dy do OS'
OSverison='alpha2.1'
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
            print(f'{disk_info[find_disk_left]["full"]}mb / {disk_info[find_disk_left]["left"]}mb left.')
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
            user_disk = input('enter new developer disk label ex(E) :')
            user_disk_full = input('enter new developer disk full mb:')
            user_disk_left=user_disk_full-1
            disk_info[user_disk] = {'full': user_disk_full, 'left': user_disk_left} #mb
    elif cmd=='system file fix':
        slect_sys_file_fix=input('real? (y,n):')
        if slect_sys_file_fix=='y':
            print('loading system file fix program...')
            print('slect system file settings')
            sys_file_fix_cmd=0
            while sys_file_fix_cmd!='exit':
                print('1.disk_in_thisPC')
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
print('safe to shutdown your PC.')
quit()