Jenkins用于持续集成 需要提前安装 JDK 和 Tomcat
* Tomcar  
将目录先移动至/Library  
cd /Library/Tomcat/bin  
开启：sudo sh ./startup.sh  
关闭：sh ./shutdown.sh
1. 解锁page：  
http://localhost:8080/  
2. 密码:  
mac装Jenkins时的密码：一定得用sudo cat查看，open不可以- -
3. 安装插件，随后创建ad和密码  
4. 构建项目  