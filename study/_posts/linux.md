* 更改Linux系统的主机名(hostname)  
`sudo vi /etc/hostname`

# vi  
: wq (输入「wq」，存盘并退出vi)  
: q! (输入q!， 不存盘强制退出vi)  
按「i」切换进入插入模式「insert mode」，按“i”进入插入模式后是从光标当前位置开始输入文件；  
「dd」：删除光标所在行。



* case
1. 当前文件夹及子目录中找出内容含“Ex”的文件并按文件大小排序。  
ls -S \`grep -Rl Ex ./* \`    
\# -S从大到小  grep：-R搜寻子目录，-l只显示文件名   利用\` \`将其作为ls的输入  
2. 11分钟后关机  
`shutdown -h +11`  


http://ju.outofmemory.cn/entry/337199
