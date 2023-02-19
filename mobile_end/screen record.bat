:: 连接多设备时，选取某个录制
@echo off 
set mdhm=%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,1%
adb devices

echo 请输入要录屏的设备名{粘贴上面的某个字母串~}

set/p var=input:

echo 请输入录屏时间（秒）:
set/p n=input:

echo ....录屏中.....
adb -s %var% shell /system/bin/screenrecord --time-limit %n% /sdcard/%mdhm%.mp4
adb -s %var% pull /sdcard/%mdhm%.mp4 D:\文档\Code\screenshot\luping
:: --time-limit：设置时间
:: -s指定序列号
echo ....完成.....
pause>nul
