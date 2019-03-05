* 更改Linux系统的主机名(hostname)  
`sudo vi /etc/hostname`

## vi  
: wq (输入「wq」，存盘并退出vi)  
: q! (输入q!， 不存盘强制退出vi)  
按「i」切换进入插入模式「insert mode」，按“i”进入插入模式后是从光标当前位置开始输入文件；  
「dd」：删除光标所在行。  
## 定时任务  
0    12   *   *   *   mail dmtsai -s "at 12:00" < /home/dmtsai/.bashrc  
#分  时   日   月  周  |《==============命令行=======================》| 

* 写了shell，怎么运行? 几种方法： 
1. 加执行权限：`chmod +x echo.sh`  
然后：在目录下`./ echo.sh`  
2. 调用解释器使得脚本执行：`bash echo.sh`  
* case
1. 当前文件夹及子目录中找出内容含“Ex”的文件并按文件大小排序。  
ls -S \`grep -Rl Ex ./* \`    
\# -S从大到小  grep：-R搜寻子目录，-l只显示文件名   利用\` \`将其作为ls的输入  
2. 11分钟后关机  
`shutdown -h +11`  


http://ju.outofmemory.cn/entry/337199
