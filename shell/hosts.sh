#修改hosts
su   #需要先进入shell才能执行以下命令
mount -o rw
remount /system
chmod 777 /etc/hosts
echo "223.111.123.229 app.***.net
120.92.168.51 api.***
111.3.86.228 data.***.com
120.199.95.225 cmask.***.com" > /etc/hosts
cat /etc/hosts   #see if success:
