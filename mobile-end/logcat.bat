adb logcat | findstr cur_vid
::利用logcat获取日志，利用管道进行过滤

:: 获取device_token
adb logcat -d | findstr BPush
:: -d:将缓存的日志输出到屏幕上, 并且不会阻塞;

::抓取崩溃日志
adb logcat *:E > D:\文档\Code\crash.txt

adb logcat | findstr /c:"new cpu name"
::/c:String  使用指定的文本作为文字搜索字符串。
pause
