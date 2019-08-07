实时查看日志
tail -f bot_bia/bia.log
最后100行
tail -100 bia.log

win10cmd切换目录

在改变目录之前，添加一个 /d 就可以跳转不同的盘符了。
cd /d c:\Users\EDZ

vim/vi操作
1.跳到文本的最后一行：按“G”,即“shift+g”
2.跳到最后一行的最后一个字符 ： 先重复1的操作即按“G”，之后按“$”键，即“shift+4”。
3.跳到第一行的第一个字符：先按两次“g”，
4.跳转到当前行的第一个字符：在当前行按“0”。
5.换行 Ctrl j
dd 删除当前行

查询某文件是否包含某条数据
 cat /opt/log/phone_white_list.txt  | grep 1522128****

 grep -v 反向搜索
 grep --help 查看帮助文档
 grep "getBeiPotentialQrcodeAddress qrCodeAddress" -C 50 dhr.log
 -C是匹配行和它前后各n行。

 上级目录 cd ..
 
