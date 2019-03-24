# what is  
Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从Apache2.0协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。  
# Docker的应用场景
Web 应用的自动化打包和发布。

自动化测试和持续集成、发布。

在服务型环境中部署和调整数据库或其他的后台应用。

从头编译或者扩展现有的OpenShift或Cloud Foundry平台来搭建自己的PaaS环境。  
# 常用命令
1. docker version

显示 Docker 版本信息。

2. docker info

显示 Docker 系统信息，包括镜像和容器数。

3. docker search
docker search [options "o">] term
docker search -s  django


从 Docker Hub 中搜索符合条件的镜像。 

4. docker pull
docker pull [-a "o">] [user/ "o">]name[:tag "o">]
docker pull laozhu/telescope:latest


从 Docker Hub 中拉取或者更新指定镜像。  

5. docker login  
root@moon:~# docker login  
Username: username  
Password: ****  
Email: user@domain.com  
Login Succeeded  
按步骤输入在 Docker Hub 注册的用户名、密码和邮箱即可完成登录。  
6. docker logout

运行后从指定服务器登出，默认为官方服务器。

7. docker images  
docker images [options "o">] [name]


列出本地所有镜像。其中 [name] 对镜像名称进行关键词查询。  

8. docker ps

列出所有运行中容器。