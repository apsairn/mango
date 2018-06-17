#	Arch Setup Functions Library
#	Writted by Python Language,Open Sourced by LGPL Linceses.
#	这个函数库允许包含在Arch Setup脚本以及其分支里。

#加载配置文件
import archsetuprc
#验证是否接受用户须知
def ul():
    if archsetuprc.linceses==True:
        return True
    else:
        print("对不起，请您接受我们的用户许可协议。")
        exit()
#分区
def part():
    print("正在执行分区操作...(正在加载CFDISK)")
    os.system("sleep 2")
    if archsetuprc.uefi==True:
        print("您使用了UEFI,真棒呀!请您稍后分区时将/dev/sda1设为EFI System,/dev/sda2为/,否则将会出现不可预料的后果！")
        print("5秒后启动CFDISK")
        os.system("sleep 3")
        os.system("cfdisk")
        print("现在您的信息将会被立刻清除并且格式化为BtrFS!")
        os.system("mkfs.vfat -F32 /dev/sda1")
        os.system("mkfs.btrfs -f /dev/sda2")
        print("分区完成!")
    else:
        print("您仍然在使用BIOS进行引导。请您稍后分区时将/dev/sda1设为可引导分区,/dev/sda2设为/,否则将会出现不可预料的后果!")
        os.system("sleep 3")
        os.system("cfdisk")
        print("现在您的信息将会被立刻清除并且格式化为BtrFS!")
        os.system("mkfs.vfat -F32 /dev/sda1")
        os.system("mkfs.btrfs -f /dev/sda2")
        print("分区完成!")

#安装基本系统
def base_inst():
    print("现在，让我们来安装基本系统。")
	#连接网络
    b=input("您要连接Wi-Fi无限局域网？(y/n)")
    if b==y:
        os.system("wifi-menu")
    else:
        os.system("dhcpcd")
    print("完成！您现在已经作好准备安装Arch Linux 用Arch Setup!")
    print("挂载文件系统...")
    os.system("mount /dev/sda2 /mnt")
    os.system("mkdir /mnt/boot")
    os.system("mount /dev/sda1 /mnt/boot")
    print("正在运行pacstrap...")
    print("正在将源修改为 清华大学开源...")
    os.system(r"echo Server =  http://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch > /etc/pacman.d/mirrorlist")
    print("完毕！正在运行Pacman...")
    os.system("pacstrap /mnt base base-devel neofetch python")
#安装桌面环境
def de():
    if archsetuprc.desktop=="gnome":
        print("正在安装 桌面环境 Gnome...")
        os.system("pacstrap /mnt gnome")
        print("完成！")
    elif archsetuprc.desktop=="kde":
        print("正在安装Qt KDE...")
        os.system("pacstrap /mnt plasma-meta")
        print("完成！")
    elif archsetuprc.desktop=="xfce":
        print("正在安装Xfce...")
        os.system("pacstrap /mnt xfce4")
        print("完成!")
    elif archsetuprc.desktop=="mate":
        print("正在安装MATE...")
        os.system("pacstrap /mnt mate")
        print("完成!")
    elif archsetuprc.desktop=="cli":
        print("没有安装 桌面环境,正在跳过...")
        print("A Skip target by Program 'Arch Setup',Widdle.")
    else:
        print("未知的桌面环境。请查看你是否选择了一个合理的桌面环境。")
        de()
#文件挂载
def genfstab():
    os.system("genfstab -U /mnt >> /mnt/etc/fstab")
#植入配置
def conf():
    print("您好！进入系统后，请执行:arch-conf")
    os.system("cp arch-conf /mnt/bin")
    os.system("arch-chroot /mnt")
    print("已经进入了Chroot系统!")
