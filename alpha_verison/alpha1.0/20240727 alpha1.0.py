#make_end time= 20240727 _PM6:08
disk_in_thisPC=[]
diskAname='dy-do-os'
diskAfull=1000 #mb #1gb
diskAleft=900 #mb
disk_in_thisPC+=['A:/']
print(f'disk A:(name={diskAname}) {diskAfull},mb/{diskAleft}mb is slected.')

diskCname='sys-full-disk'
diskCfull=0
while not(str and diskCfull>=1000 and diskCfull<=250000):
    diskCfull=int(input(f'enter {diskCname} disk mb (1000+ 250000-):'))
diskCfull=int(diskCfull)
diskCleft=diskCfull-1
disk_in_thisPC+=['C:/']

PCname=input('enter your PCname:')


print('importing...')
import time
import tkinter as tk
from tkinter import messagebox
print('loading dy do OS...')
CMDhelp=["index(CMDhelp) = help of cmd.", "index(shutdown/help) = see help for shutdown menu.", "disk_left = print disk left (input) drive", "log-out = log out this user."]
OSname='dy do OS'
OSverison='1.0'
print('hello, user')
print("help cmd to 'index(CMDhelp)'.")
print("this verison is test verison of 'dy do OS'.")
cmd=''
while cmd!='exit':
    cmd=input('C:/')
    if cmd=='index(CMDhelp)':
        print('index of CMDhelp')
        print(CMDhelp)
    elif cmd=='index(shutdown/help)':
        print("shutdown computer to 'shutdown -s -c'.")
    elif cmd=='shutdown -s -c':
        print('dy do OS is shutdowning...')
        cmd='exit'
    elif cmd=='disk_left':
        print('slect disk')
        print(disk_in_thisPC)
        find_disk_left=input(':')
        if find_disk_left in disk_in_thisPC:
            if find_disk_left=='A:/':
                print(diskAfull,'mb/',diskAleft, 'mb left')
            elif find_disk_left=='C:/':
                print(diskCfull,'mb/',diskCleft, 'mb left')
        else:
            print(f'no drive {disk_in_thisPC} in this PC.')
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
            cmd='exit'

print('safe to shutdown your PC.')
quit()