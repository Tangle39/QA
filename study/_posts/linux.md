## Q:linux开机过程？  
1. 加载BIOS（Basic Input Output System）  
2. 读取MBR（Main Boot Record）  
3. Boot Load  
4. 加载内核  
5. 用户层init依据inittab文件来设定运行等级  
6. init进程执行rc.sysinit  
7. 启动内核模块  
8. 执行不同运行级别的脚本程序  
9. 执行/etc/rc.d/rc.local  
10. 执行/bin/login程序，进入登录状态

## vi  
: wq (输入「wq」，存盘并退出vi)  
: q! (输入q!， 不存盘强制退出vi)  
按「i」切换进入插入模式「insert mode」，按“i”进入插入模式后是从光标当前位置开始输入文件；  
「dd」：删除光标所在行。  
## 定时任务  

<table>
        <tr>
            <th>0</th>
            <th>12</th>
            <th>*</th>
            <th>*</th>
            <th>*</th>
            <th>mail dmtsai -s "at 12:00" < /home/dmtsai/.bashrc</th>
        </tr>
        <tr>
            <th>分</th>
            <th>时</th>
            <th>日</th>
            <th>月</th>
            <th>周</th>
            <th>《==============命令行=======================》</th>
        </tr>
    </table>   

## 写了shell，怎么运行? 几种方法:  

1. 加执行权限：`chmod +x echo.sh`  
然后：在目录下`./ echo.sh`,也可以绝对路径`/.../.../echo.sh`    

2. 调用解释器使得脚本执行：`bash echo.sh`，或者`sh ./**.sh`  

## rsync  
rsync是linux系统下的数据镜像备份工具。使用快速增量备份工具Remote Sync可以远程同步，支持本地复制，或者与其他SSH、rsync主机同步。

## 后台执行命令
为了使这些进程能够在后台运行，也就是说不在终端屏幕上运行，有几种选择方法可供使用  
* &
在命令后面加上& 实现后台运行。例如：sh test.sh &  
* nohup
使用&命令后，作业被提交到后台运行，当前控制台没有被占用，但是一但把当前控制台关掉(退出帐户时)，作业就会停止运行。  
所以使用：  
nohup command &  
在缺省情况下该作业的所有输出都被重定向到一个名为nohup.out的文件中

## case  

1. 当前文件夹及子目录中找出内容含“Ex”的文件并按文件大小排序。  
ls -S \`grep -Rl Ex ./* \`  
\# -S从大到小 ; grep：-R搜寻子目录，-l只显示文件名 ;  利用\` \`将其作为ls的输入  ; 少\*会多一个/  
grep -n:结果输出行号

2. 11分钟后关机  
`shutdown -h +11`  

3. 更改Linux系统的主机名(hostname)  
`sudo vi /etc/hostname`  
4. 显示当前目录下的所有文件及文件夹包括隐藏的.和..等的详细信息  
`ls -al`  
5. arp(Address Resolution Protocol)  
arp命令用于操作主机的arp缓冲区，可以用来显示arp缓冲区中的所有条目、删除指定的条目或者添加静态的ip地址与MAC地址对应关系。  
查看ARP缓存记录的命令  
`arp -a`  
6. 重新启动Linux系统的同时把内存中的信息写入硬盘  
shutdown -r now  
shutdown命令可以**安全地**关闭或重启Linux系统  
使用reboot命令可以快速地关闭系统，但如果还有其它用户在该系统上工作时，就会引起数据的**丢失**。所以使用reboot命令的场合主要是在**单用户**模式。  
7. 切换目录  
home:cd ~  
根目录:cd /  
8. 帮助类命令  
ls --help  
man ls(更详细)  
9. 重定向 将当前目录的文件存至某一路径：  
ls >> /Users/lu/Documents/Code/linux/test.txt(>为覆盖；>>追加)  
10. 列出当前目录以及子目录下所有扩展名为“.txt”的文件  
find . -name "\*.txt"  
11. 利用管道符计算1+2+3+...+100的值  
echo {1..100} |tr ' ' '+'| bc   
\# tr:替换，   bc：linux计算器  


>reference  
http://ju.outofmemory.cn/entry/337199  
https://www.cnblogs.com/shishanyu/p/7966975.html
