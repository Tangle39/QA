目前最主流的三个Web服务器是Apache、 Nginx 、IIS  
# 前端数据存储方式  
* 服务端存储
cache :缓存(存放在内存中)，将DB或磁盘中的数据放在缓存中访问，减少磁盘IO  
磁盘文件：资源文件：如图片和视频  
数据库： 如MySQL和与node.js配合的MongoDB :记录表查询  
内存： 频繁访问的资源，提高读取效率  
* 客户端存储
1. H5之前
cookies  
特点:  
a. 在每次http请求头上都会带着：三次握手等请求响应，一直带着cookie比较臃肿，而且会存在安全问题  
b. 对每个域名，客户端只会存4K大小的cookie，存储量小  
c. 主Domain(域名)污染：如果数据存放在主域名之下，则所有资源名有http请求时，请求头都会带着主域名存在cookie中的数据，会造成主域名cookie的污染  
2. H5  
a. 本地存储(localstorage && sessionstorage)  
核心API：localStorage对象 && sessionStorage对象  
b. 离线缓存(application cache) APP cache   
Appcache是从浏览器的缓存中分离出来的一块缓存区  
API的核心是applicationCache对象  
它可以让Web应用在离线的情况下继续使用，通过manifest文件指明需要缓存的资源  
c. IndexedDB 和 Web SQL

# 当你打开一个网页  

* 第一步  
  输入网址了，那么对于浏览器来说，这是它唯一的线索，也就是URL。URL全称Unified Resource Locator，翻译过来就是统一资源定位符，俗称网址。  
* 第二步   
  当浏览器去找网页的时候，首先需要去服务器上找网页，那么网页在哪里呢？ 存储网页的地方叫做服务器(Server)，服务器本身也是电脑，但是比个人电脑的性能要高很多。  
  服务器也有多个，怎么找呢？就是根据给出的URL了。但其实，URL只是服务器地址的一个好记的名字而已，必须将URL解析为IP地址，才能找到相应的服务器。打个比方，URL好比是饭店的店名，那么IP地址就是是饭店的门牌地址。从URL到IP地址的过程叫做DNS查找，也就是DNS Lookup  
* Connect & Request  
  根据IP找到服务器后，就可以向服务器发送请求了，请求服务器将你需要的网页发还给浏览器，浏览器和服务器传输信息的方式，就是建立连接。就像有个通道来供服务器和浏览器传递信息。  
  建立连接后，浏览器向服务器发起一个request请求，在请求中，需要告诉服务器想要的资源是什么，比如，我们请求google的首页：http://google.com:80/path?q=a#hash    
  一个URL一般由6个部分组成：协议、主机名、端口号、资源位置、queryString、hashTag;不同的path代表不同的资源，一般指页面，比较特殊的 / 是指根路径，一般会是网站的首页，和在电脑文件夹路径是同样的。    在前面所说的request请求中，包含一些数据:  
  GET / HTTP/1.1  
  Host: google.com  
  Accept:*/*  
  Pragma: no-cache  
  Cache-Control: no-cache  
  User-Agent:Mozilla/4.04[en](Win95;I;Nav)  
  GET/指从服务器上请求一个资源，这个资源的位置是/,另外，Host:google.com代表请求的主机名是google.com    
* Web Server     
  当服务器收到请求之后，经过Web Server对请求进行处理，最后将所请求的资源打包起来通过通道返回给浏览器。  每台服务器上都有Web Server用以处理请求，常见的有apache、nginx、IIS或Lighttpd等。  
    Web Server对于不同用户发送的请求，会结合配置文件，把不同请求委托给服务器上处理对应请求的程序进行处理（如CGI脚本，JSP脚本，servlets，ASP脚本，服务器端JavaScript等），然后返回后台程序处理产生的结果作为Response返回给浏览器。  
    现有后台处理程序大部分都使用了MVC框架：模型(Model) - 视图(View) - 控制器(Controller)；MVC是一种设计模式，三个部分的组件各自处理自己的任务，从而将输入、处理和输出分离。  
    控制器接收浏览器的请求，决定应该调用哪个模型来进行处理，然后模型用业务逻辑来处理用户的请求并返回数据，最后控制器用相应的视图格式化模型返回html字符串给浏览器，这个返回的数据，叫做响应(Response)。  
  Response和Request是对应的，响应也包含和请求类似的数据：  
  HTTP/1.0200OK  
  Date:Mon,31Dec200104:25:57GMT  
  Server:Apache/1.3.14(Unix)  
  Content-type:text/html  
  Last-modified:Tue,17Apr200106:46:28GMT  
  Etag:"a030f020ac7c01:1e9f"  
  Content-length:39725426  
  Content-range:bytes554554-40279979/40279980  
  响应分为两个部分：响应头和响应主体。其中网页的代码包含在响应主体中。
* 浏览器处理及渲染  
  浏览器收到Response后，首先对其进行加载，并根据其中的代码继续向服务器请求资源(css、javascript、img等)，加载完成后对页面进行解析。  
  解析的过程，其实就是生成解析树，即Dom树。Dom树是由Dom元素及属性节点组成，加上css解析的样式对象和js解析后的动作实现。  
  接下来对Dom树进行可视化表示，也就是渲染，生成一颗渲染树。    最后一步就是绘制网页，浏览器根据渲染树将元素绘制到屏幕上，同时执行js，完成整个页面的展示。

# Restful api

REST，即Representational State Transfer的缩写。直接翻译的意思是"表现层状态转化"。  
它是一种互联网应用程序的API设计理念：URL定位资源，用HTTP动词（GET,POST,DELETE,DETC）描述操作。  
即:  
url地址中只包含名词表示资源，使用http动词表示动作进行操作资源  
常用的HTTP动词有下面五个  

* GET（SELECT）：从服务器取出资源（一项或多项）。
* POST（CREATE）：在服务器新建一个资源。
* PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
* PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
* DELETE（DELETE）：从服务器删除资源。

# GET请求和POST请求的区别：

```markdown
GET使用URL或Cookie传参。而POST将数据放在BODY中。  
ET的URL会有长度上的限制，则POST的数据则可以非常大。  
OST比GET安全，因为数据在地址栏上不可见。  
一般get请求用来获取数据，post请求用来发送数据。  
```

凡事无绝对，只有最后一点说的是比较靠谱的  

# http状态码

每发出一个http请求之后，都会有一个响应，http本身会有一个状态码，来标示这个请求是否成功，常见的状态码有以下几种：  
1、200 2开头的都表示这个请求发送成功，最常见的就是200，就代表这个请求是ok的，服务器也返回了。  
2、300 3开头的代表重定向，最常见的是302，把这个请求重定向到别的地方了  
3、400 400代表客户端发送的请求有语法错误，401代表访问的页面没有授权，403表示没有权限访问这个页面，404代表没有这个页面 
4、500 5开头的代表服务器有异常，500代表服务器内部异常，504代表服务器端超时，没返回结果  