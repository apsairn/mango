#	Arch Setup Tool,2018 Copyright All.
#	This Software is Open Sourced by GNU GPL 2.0 Linceses.
#	This is the 'Arch Setup' Profile.
import os
##User Linceses
#请不要收费售卖这个脚本以及其分支。
#请不要修改这个脚本但生成是官方的。
#使用这个脚本时，请遵守GNU GPL 2.0协议。

#是否接受以上许可
linceses=False	#默认为不接受，请你修改为True

#UEFI支持
uefi=False	#默认为不支持UEFI

#桌面环境(gnome / plasma / xfce / mate / cli)
desktop=None

#用户自定义的钩子
def hook():
    #空的
    print("无钩子")
