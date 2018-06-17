首先,应该去下载一个最新的Arch Linux LiveCD。我们可以去mirror.tuna.tsinghua.edu.cn下载一个Arch LiveCD，这一步不详细解释，我相信你们会的。
然后，重点来了。需要刻录。如果你是Windows 系统,请下载Rufus并刻录,千万不要用UltraISO！如果你是Linux系统,就只需要打出以下指令:
dd if=<ISO的位置> of=/dev/sdb
稍等片刻,刻录完毕时,便可重启。
# 正式安装
现在，应该可以正式的安装了。从USB启动，进入Arch Linux LiveCD，安装！
## 网络实验
执行以下命令来测试你的网络环境是否已经配置完毕：
>ping archlinux.org

如果你失败了,那么有限网络执行dhcpcd,无线网络执行wifi-menu。
## 硬盘分区
首先,你应该给Arch Linux分一个主分区。执行以下命令进入图形界面分区:
>cfdisk

如果你是BIOS，那么分一个可引导和一个主分区,如果你是UEFI，那么分一个EFI 
System和一个主分区。
## 格式化分区
你只需执行以下命令:(一律将/dev/sda1是为引导,/dev/sda2视为主分区)
>mkfs.btrfs -f /dev/sda2
>mkfs.vfat -F32 /dev/sda1

## 挂载分区
执行下面的命令来挂载分区:
>mount /dev/sda2 /mnt
>mkdir /mnt/boot
>mount /dev/sda1 /mnt/boot

## 源
默认的官方源由于服务器在国外,因此速度很慢。我们应该将源更换为Tsinghua源，这样就很快了。在/etc/pacman.d/mirrorlist第一行写上:
>Server = https://mirror.tuna.tsinghua.edu.cn/archlinux/$repo/$arch
这样，在稍后执行pacstrap时十分钟就可以完成了。
## Pacstrap
执行以下命令:
>pacstrap /mnt base base-devel

## FSTAB
为了在系统启动时自动挂载文件系统也就是fstab,需要执行以下命令:
>genfstab -U /mnt > /mnt/etc/fstab

了解fstab的朋友可以执行以下命令来看看生成的fstab是否正确:
>cat /mnt/etc/fstab

## 进入安装好的系统
执行以下命令来进入Chroot环境:
>arch-chroot /mnt

## 时间
你是否经常看时间呢？执行下面的命令来执行自动对时吧!
>ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

建议生成/etc/adjtime:
>hwclock --systohc
## 区域和语言
执行以下命令来设置区域和语言为中国:
>echo zh_CN.UTF-8 UTF-8 >/etc/locale.gen
>locale-gen
>echo LANG=zh_CN.UTF-8 > /etc/locale.conf

# 网络配置
## 主机名
执行以下命令可以设置你的主机名：
>echo <主机名> >/etc/hostname

# ROOT密码
执行以下命令来给Root 用户设置密码:
>passwd root

# 普通用户
你应该有一个普通用户来确保系统的安全性。如果root常年使用的话，可能会不保系统安全性。因此，使用以下命令创建新用户:
>useradd -m <用户名>
>passwd <用户名>

为了让这个普通用户方便的使用root权限,应该配置sudo。执行以下命令修改sudo配置文件:
>nano /etc/sudoers

#安装Gnome
现在，执行以下命令:
>pacman -S gnome wqy-microhei wqy-zenhei network-manager-applet

好了。
# 安装中文输入法
执行下面的命令:
>pacman -S ibus-libpinyin

稍后在GNOME的设置里将输入法修改为智能拼音即可。
# 开启必要的服务
>systemctl enable gdm
>systemctl enable NetworkManager

# 引导管理
这里我们选择grub,安装软件包efibootmgr和grub，跟着做。
## BIOS
执行：
>grub-install --target=i386-pc /dev/sda

如果没有报错，那就是成功了，可喜可贺!
## UEFI
执行:
>grub-install --target=x86_64-efi --efi-directory=/boot bootloader-id=Arch

无论是BIOS,还是UEFI,都要执行一条命令:
>grub-mkconfig -o /boot/grub/grub.cfg

# 配置
重启后，便可安装自己喜欢的应用，配备自己喜欢的主题，完毕 !
# End
## The End
### Really End
