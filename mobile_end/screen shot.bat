:: 用来截屏-安卓
:: "::"可以用来注释~ 但是最好单独分行
@echo off      
echo .........截屏中.........
echo 文件名格式 月日时分秒
set mdhm=%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,1%
adb shell /system/bin/screencap -p /sdcard/%mdhm%.png
:: screencap:adb的截图命令
adb pull /sdcard/%mdhm%.png D:\文档\Code\screenshot
pause
:: pause使得窗口可以不消失
