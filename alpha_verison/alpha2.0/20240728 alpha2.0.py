disk_in_thisPC=[]
diskCname='dy-do-os'
diskCfull=1000 #mb #1gb
diskCleft=900 #mb
disk_in_thisPC+=['C:/']
print(f'disk C:(name={diskCname}) {diskCfull},mb/{diskCleft}mb is slected.')

diskDmaked=0

PCname=input('enter your PCname:')

print('importing...')
import time
import tkinter as tk
from tkinter import messagebox
print('loading dy do OS...')
CMDhelp=["index(CMD/help) = help of cmd.", "index(shutdown/help) = see help for shutdown menu.", "disk left = print disk left (input) drive", "log-out = log out this user."]
OSname='dy do OS'
OSverison='alpha1.1'
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
        print('slect disk')
        print(disk_in_thisPC)
        find_disk_left=input(':')
        if find_disk_left in disk_in_thisPC:
            if find_disk_left=='C:/':
                print(f'index of {find_disk_left} full/left')
                print(f'{diskCfull}mb / {diskCleft}mb left.')
            elif find_disk_left=='D:/':
                print(f'index of {find_disk_left} full/left')
                print(f'{diskDfull}mb / {diskDleft}mb left.')
            else:
                print(f'{find_disk_left} disk is not in the PC.')
        else:
            print(f'{find_disk_left} disk is not in the PC.')
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
        if diskDmaked==0:
            diskDname='sys-full-disk'
            diskDfull=0
            while not(str and diskDfull>=1000 and diskDfull<=250000):
                diskDfull=int(input(f'enter {diskDname} disk mb (1000+ 250000-):'))
            diskDfull=int(diskDfull)
            diskDleft=diskDfull-1
            disk_in_thisPC+=['D:/']
            diskDmaked=1
        elif diskDmaked==1:
            print(f'disk D drive is maked later.')
        else:
            print(f'err.sys.Ddrive.make.0or1.not')
            quit()
    elif cmd=='system file fix':
        slect_sys_file_fix=input('real? (y,n):')
        if slect_sys_file_fix=='y':
            print('loading system file fix program...')
            print('slect system file settings')
            sys_file_fix_cmd=0
            print('1.diskDmaked')
            print('2.diskDname')
            while sys_file_fix_cmd=='exit':
                sys_file_fix_cmd=input(':')
                if sys_file_fix_cmd=='diskDmaked':
                    print('input diskDmaked variable (new)')
                    sys_file_fix_diskDmaked_new=input(':')
                    diskDmaked=sys_file_fix_diskDmaked_new
                elif sys_file_fix_cmd=='diskDname':
                    print('input diskDname variable (new)')
                    sys_file_fix_diskDname_new=input(':')
                    diskDname=sys_file_fix_diskDname_new
                else:
                    print('sys.file.fix.command.not')
        elif slect_sys_file_fix=='n':
            print('OK.')
        else:
            print('err.sys.file.fix.program.slect.yorn')
print('safe to shutdown your PC.')
quit()