# 为什么使用微服务
单体应用随着发展变成巨型应用，扩展十分艰难，使用微服务解决其复杂性  
优点：  
* 解决复杂性问题
* 使得每个服务可以被独立地开发
* 每个微服务可以独立部署
* 每个服务独立扩展

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

# k8s
对Docker及容器进行更高级更灵活的管理，是基于容器的集群管理平台，它的全称，是kubernetes。  
一个K8S系统，通常称为一个K8S集群（Cluster）。  
主要包括两个部分：

* 一个Master节点（主节点）
* 一群Node节点（计算节点）
Master节点包括API Server、Scheduler、Controller manager、etcd。  
Node节点包括Docker、kubelet、kube-proxy、Fluentd、kube-dns（可选），还有就是Pod。  

# SpringCloud
spring cloud 为开发人员提供了快速构建分布式系统的一些工具，包括配置管理、服务发现、断路器、路由、微代理、事件总线、全局锁、决策竞选、分布式会话等等  
* Spring Cloud核心组件：Eureka
Eureka Client：负责将这个服务的信息注册到Eureka Server中  
Eureka Server：注册中心，里面有一个注册表，保存了各个服务所在的机器和端口号  
各个服务启动时，Eureka Client都会将服务注册到Eureka Server，并且Eureka Client还可以反过来从Eureka Server拉取注册表，从而知道其他服务在哪里  
* Spring Cloud核心组件：Feign
基于Feign的动态代理机制，根据注解和选择的机器，拼接请求URL地址，发起请求 
* Spring Cloud核心组件：Ribbon
使用Round Robin轮询算法，合理访问机器
* Spring Cloud核心组件：Hystrix
处理服务异常，熔断，降级  
发起请求是通过Hystrix的线程池来走的，不同的服务走不同的线程池，实现了不同服务调用的隔离，避免了服务雪崩的问题  
* Spring Cloud核心组件：Zuul
如果前端、移动端要调用后端系统，统一从Zuul网关进入，由Zuul网关转发请求给对应的服务  
![image](https://github.com/entangle1993/QA/blob/master/image/sc.jpg)
