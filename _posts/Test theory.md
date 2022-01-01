# 白盒测试  
六种覆盖方法中，覆盖准则由弱到强依次是语句覆盖、判定覆盖（分支覆盖）、条件覆盖、判定/条件覆盖、条件组合覆盖、路径覆盖。  
* 边界值法白盒黑盒均适用  

# 黑盒测试
1. 等价类划分测试
* 有效等价类
* 无效等价类
2. 边界值分析
3. 决策表测试？
4. 因果图

# 分类  
按开发阶段分为单元测试，集成测试，确认测试，系统测试，验收测试。  
单元测试：根绝详细设计来设计用例  
ps：单元测试-详细设计 集成测试-概要设计 确认测试，系统测试-需求文档 验收测试-用户需求  
# QPS
Query Per Second  

0902
B/S架构 即浏览器和服务器架构模式，有比C/S更强的适应范围，一般只要有操作系统和浏览器就行。  
C/S 服务器-客户机  客户端需要安装专用的客户端软件。两端的通讯速度和通讯的效率大大的提高

# 测试的各种类型

What is Shakeout testing? This test is basically carried out to check the networking facility, database connectivity and the integration of modules. The Configuration Management team, who prepare builds for test environments, normally does this test. They also test whether the major components of the software are not broken. This test is done BEFORE the build is deployed in the test environment. After the shake out testing, the next step is smoke testing (which is done by the testers after the build is deployed in the test environment)

## 什么是接口测试？

接口测试就是通过测试不同情况下的入参与之相应的出参信息来判断接口是否符合或满足相应的功能性、安全性要求。  

* 接口组成:  
  1、接口说明  
  2、调用url  
  3、请求方法（get/post）  
  4、请求参数、参数类型、请求参数说明  
  5、返回参数说明  

## 常见接口：

1、webService接口：是走soap协议通过http传输，请求报文和返回报文都是xml格式的，我们在测试的时候都用通过工具才能进行调用，测试。可以使用的工具有SoapUI、jmeter、loadrunner等；

2、http api接口：是走http协议，通过路径来区分调用的方法，请求报文都是key-value形式的，返回报文一般都是json串，有get和post等方法，这也是最常用的两种请求方式。可以使用的工具有postman、RESTClient、jmeter、loadrunner等；

## 接口自动化框架

1.结构（框架思想（数据，关键字，行为，事件，混合）)

2.读取用例的模块（excel，txt,mysql,xml）

3.发请求的模块（requests封装）

4.断言模块（re，遍历断言）

5.日志模块

6.测试报告生成模块

7.发邮件模块

8.配置文件  

## 性能工具：Jmeter、loadrunner、Locust

* Jmeter建立测试脚本:  

1. 测试计划→添加线程组  
   线程数：虚拟用户数，一个虚拟用户占用一个进程或线程。设置多少虚拟用户数在这里也就是设置多少个线程数  
   Ramp-Up Period(in seconds)：设置的虚拟用户数需要多长时间全部启动。如果线程数为10 ，Ramp-Up Period为100，那么就是100秒钟内启动10个线程。每一个线程都会在上一个线程启动10秒钟后才开始运行；设置为0则表示同时启动  
   Ramp-Up Period(in secods)不能设置太小的数值，否则会一开始就给服务器过大的压力；也不能设置太大的数值，否则第一个线程已经执行完了，最后一个还没启动的情况）刚开始Ramp-Up值可以等于总线程数，之后再作调整  
   循环次数：每个线程发送请求的次数，如果线程数为20 ，循环次数为100，那么每个线程发送100次请求。总请求数为20*100=2000。如果勾选了“永远”，那么所有线程会一直发送请求，一到选择停止运行脚本  
   启动时间：线程运行的起始时间  
   结束时间：线程运行的结束时间  
   持续时间：设置了持续时间则启动时间会失效  
   启动延迟：设置了启动延迟则结束时间会失效  
   eg:线程数1000循环1次与线程数10循环100次的区别：线程数1000循环1次可以选择并发；线程数10循环100次是类似于长时间施加压力  
2. 添加HTTP请求并设置  
   添加：sampler：http请求  
   http 默认端口80，https默认端口443  
3. 添加http信息头管理器并设置  
   添加配置原件：http信息头管理器  
   网站(csdn)只接受浏览器发的请求，所以要用到浏览器头信息（不加这个头，返回403，响应被拒）  
   下面是python脚本里常用的，可以选择一个拷贝过去  
        my_headers = [  
        'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',  
        'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',  
        'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',  
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']  
        header = {"User-Agent": random.choice(my_headers)}  
4. 添加查看结果树：  
   监听器：察看结果树  
   有响应数据等  
5. 添加聚合报告  
   90%Line：所有请求响应时间按升序排序后，90%时最大响应时间（ms）  
   是满足需求响应时间的重要指标

## jmeter性能指标分析

（服务器监控插件）

1. Active Threads Over Time：不同时间的活动用户数量展示（图表）
2. AutoStop Listener ：自动停止监听器
   设置当发生某些预期之外的情况时自动停止测试  
3. Bytes Throughput Over Time:不同时间吞吐量
4. Composite Graph： 混合图表  
5. Flexible File Writer：这个插件允许你灵活记录测试结果 
6. Hits per Second：每秒点击量  
7. jp@gc  (插件）PerfMon Metrics Collector：服务器性能监测控件
8. Reponse Latencies Over Time：记录客户端发送请求完成后，服务器端返回请求之前这段时间
   。。。
9. 聚合报告
   lable：对应每一个http请求，显示的是http请求的Name，如百度http请求name为baidu

Samples：表示这一次的测试中一共发出了多少请求，如上图所示，sougou和baidu的http请求每个都发出30个请求

Average：平均响应时间，指的是所有的请求的平均响应时间，如上图的30个请求的总的响应时间除以30得出的平均响应时间，默认的情况下是单个请求的平均响应时间，但当使用了“事务控制器”时，则以事物为单位显示平均响应时间

Median：中位数，也就是50%用户的响应时间

90%Line：90%用户的响应时间

Min：最小响应时间

Max：最大的响应时间

Error%：本次测试中出现错误的请求的数量/请求的总数，如上图所示，本次的测试中，sougou的http请求66.6%的请求出错，而baidu的请求则没有出错的请求

Throughput：吞吐量，默认情况下表示每秒完成的请求数，如上图所示，每秒完成的请求数分别为6.6个每秒，6.2个每秒

Recived KB/Sec：每秒从服务器端接收到的数据量，以kb为计算的单位

# 测试框架

__Selenium__ is a free (open source) Test automation library. It is used to automate Web and Mobile environments. It consists of

1. Selenium IDE (Browser Addon – Record and Playback Tool)
2. Selenium WebDriver
3. Selenium Grid (Distributed Testing)

Appium:移动端自动化框架  
__Robot framework__:主要用于轮次很多的验收测试和验收测试驱动开发（ATDD）,可用于接口测试  
__Junit__:为 Java 代码编写单元测试  
REST Assured:对于 REST API 集成测试来说是一个很好的工具。(RESTful service是一种架构模式，近几年比较流行了，它的轻量级web服务，发挥HTTP协议的原生的GET，PUT，POST，DELETE。)  

__TestNG__:源于 JUnit 和 NUnit 的启发，但它在这两者的基础上引入了许多新的功能;随着 JUnit 4 中注解功能的引入以及 Hamcrest 框架的整合，JUnit 4 和 TestNG 之间的差距已经很小。  
__Mockito__:Mock 测试是现代单元测试的关键技术之一  
__Spock__ 框架:用于 Java 和 Groovy 应用程序的测试和规范框架  
__Katalon Studio__:一款功能强大的测试自动化解决方案，适用于Web应用程序，移动和Web服务。 基于Selenium和Appium框架构建，Katalon Studio利用这些解决方案实现集成软件自动化。

__Espresso__是Google官方提供并推荐的Android测试库，它是一个AndroidJunit单元测试库，用于Android仪器化测试，即需要运行到设备或模拟器上进行测试。

__UI Testing__:iOS  UI 自动化测试框架

# 测试工具

## Jmeter

* Jmeter建立测试脚本:  

1. 测试计划→添加线程组  
   线程数：虚拟用户数，一个虚拟用户占用一个进程或线程。设置多少虚拟用户数在这里也就是设置多少个线程数  
   Ramp-Up Period(in seconds)：设置的虚拟用户数需要多长时间全部启动。如果线程数为10 ，Ramp-Up Period为100，那么就是100秒钟内启动10个线程。每一个线程都会在上一个线程启动10秒钟后才开始运行；设置为0则表示同时启动  
   Ramp-Up Period(in secods)不能设置太小的数值，否则会一开始就给服务器过大的压力；也不能设置太大的数值，否则第一个线程已经执行完了，最后一个还没启动的情况）刚开始Ramp-Up值可以等于总线程数，之后再作调整  
   循环次数：每个线程发送请求的次数，如果线程数为20 ，循环次数为100，那么每个线程发送100次请求。总请求数为20*100=2000。如果勾选了“永远”，那么所有线程会一直发送请求，一到选择停止运行脚本  
   启动时间：线程运行的起始时间  
   结束时间：线程运行的结束时间  
   持续时间：设置了持续时间则启动时间会失效  
   启动延迟：设置了启动延迟则结束时间会失效  
   eg:线程数1000循环1次与线程数10循环100次的区别：线程数1000循环1次可以选择并发；线程数10循环100次是类似于长时间施加压力  
2. 添加HTTP请求并设置  
   添加：sampler：http请求  
   http 默认端口80，https默认端口443  
3. 添加http信息头管理器并设置  
   添加配置原件：http信息头管理器  
   网站(csdn)只接受浏览器发的请求，所以要用到浏览器头信息（不加这个头，返回403，响应被拒）  
   下面是python脚本里常用的，可以选择一个拷贝过去  
        my_headers = [  
        'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',  
        'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',  
        'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',  
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']  
        header = {"User-Agent": random.choice(my_headers)}  
4. 添加查看结果树：  
   监听器：察看结果树  
   有响应数据等  
5. 添加聚合报告  
   90%Line：所有请求响应时间按升序排序后，90%时最大响应时间（ms）  
   是满足需求响应时间的重要指标

### jmeter性能指标分析

（服务器监控插件）

1. Active Threads Over Time：不同时间的活动用户数量展示（图表）
2. AutoStop Listener ：自动停止监听器
   设置当发生某些预期之外的情况时自动停止测试  
3. Bytes Throughput Over Time:不同时间吞吐量
4. Composite Graph： 混合图表  
5. Flexible File Writer：这个插件允许你灵活记录测试结果 
6. Hits per Second：每秒点击量  
7. jp@gc  (插件）PerfMon Metrics Collector：服务器性能监测控件
8. Reponse Latencies Over Time：记录客户端发送请求完成后，服务器端返回请求之前这段时间
   。。。
9. 聚合报告
   lable：对应每一个http请求，显示的是http请求的Name，如百度http请求name为baidu

Samples：表示这一次的测试中一共发出了多少请求，如上图所示，sougou和baidu的http请求每个都发出30个请求

Average：平均响应时间，指的是所有的请求的平均响应时间，如上图的30个请求的总的响应时间除以30得出的平均响应时间，默认的情况下是单个请求的平均响应时间，但当使用了“事务控制器”时，则以事物为单位显示平均响应时间

Median：中位数，也就是50%用户的响应时间

90%Line：90%用户的响应时间

Min：最小响应时间

Max：最大的响应时间

Error%：本次测试中出现错误的请求的数量/请求的总数，如上图所示，本次的测试中，sougou的http请求66.6%的请求出错，而baidu的请求则没有出错的请求

Throughput：吞吐量，默认情况下表示每秒完成的请求数，如上图所示，每秒完成的请求数分别为6.6个每秒，6.2个每秒

Recived KB/Sec：每秒从服务器端接收到的数据量，以kb为计算的单位

### Jmeter获取数据的几种方法

1、手动写入

2、正则表达式提取器

3、Json提取

4、读取文件

5、数据库查询

6、使用随机数和计数器...

## Protractor

Protractor is an end-to-end test framework for Angular and AngularJS applications.

Protractor is a [Node.js](http://nodejs.org/) program.

## QTP

自动测试工具

# Questions

**Explain what is traceability matrix?**

A test matrix is used to map test scripts to requirements.

# 测试策略

测试策略：侧重需求分析，评估风险，定义测试范围，确定测试方法，制定测试启动、停止、完成标准和条件。  
项目A:  
![项目示意图](C:/Users/TANGLELU/Documents/GitHub/QA/_posts/项目示意图.jpg)  

1. 开始  
   收集更多信息  

* 项目的范围  
* 人力投入  
* 历史情况  
* ……  

2. “四步测试策略制定法”  
   明确产品质量目标  
   风险分析  
   适配产品开发流程  
   测试分层  
3. 制定总体测试策略  
   优先级
4. 制定阶段测试策略  
   验收测试策略  

# 设计（功能）测试用例的思路


举例：

我想要回家，让你给我买一张票，然后设计测试用例

答案：

1.确定需求(回家回哪，需要什么票，买什么时候的票)

2.开始测试

2.1功能测试（我去买票（买火车票，飞机票），买到票（什么时候），回来给你）

2.2可靠性测试（我去买票过程中被撞死了，票买不到怎么办，延期了，买那个点的票没了怎么办让我帮他买票的人的身份，比如是否有特殊优待，如军人，1米2以下儿童等，身份证丢了，或者票丢了，责任划分）

2.3可维护性测试（票是否可保存完好）

2.4兼容性（换不同人的去买，我中间招人去买，我坐车走路）

2.5算法测试（我通过不同的渠道买票花费的时间）

2.6竞品测试（别的人怎么买的票）

2.7安全性测试（身份信息保密）

2.8性能测试（一个身份证买多张票，同时多张身份证买多张票）

参考：https://blog.csdn.net/qq_30758629/article/details/81568366

# 敏捷开发

敏捷开发以用户的需求进化为核心，采用迭代、循序渐进的方法进行软件开发。在敏捷开发中，软件项目在构建初期被切分成多个子项目，各个子项目的成果都经过测试，具备可视、可集成和可运行使用的特征。换言之，就是把一个大项目分为多个相互联系，但也可独立运行的小项目，并分别完成，在此过程中软件一直处于可使用状态。