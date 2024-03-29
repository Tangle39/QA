[TOC]

# Mysql

## 连接

进入本机mysql数据库：
/usr/local/MySQL/bin/mysql -u root -p

## 创建数据库

```mysql
CREATE DATABASE 数据库名;
```

## 删除数据库

```mysql
drop database <数据库名>;
```

## 选择数据库

`use 数据库名;`

## 插入数据

```mysql
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```

# 事务

事务是一系列的操作,他们要符合ACID特性.最常见的理解就是:事务中的操作要么全部成功,要么全部失败.

## 事务(Transaction)四大特性

原子性，要么执行，要么不执行
隔离性，所有操作全部执行完以前其它会话不能看到过程
一致性，事务前后，数据总额一致
持久性，一旦事务提交，对数据的改变就是永久的

## 数据库隔离级别

***如果不考虑隔离性，会发生什么事呢？***【同时有多个事务在进行】

脏读(Read out of invalid data)：事务B读取事务A还没有提交的数据
不可重复读：两次事务读的数据不一致（事务A首先读取了一条数据，然后执行逻辑的时候，事务B将这条数据改变了，然后事务A再次读取的时候，发现数据不匹配了，就是所谓的不可重复读了）
幻读:事务A修改了数据，事务B也修改了数据，这时在事务A看来，明明修改了数据，咋不一样

***四种隔离级别解决了上述问题***

1.读未提交（Read uncommitted）：

这种事务隔离级别下，select语句不加锁。

此时，可能读取到不一致的数据，即“***读脏*** ”。这是并发最高，一致性最差的隔离级别。

 2.读已提交（Read committed）：

可避免 ***脏读*** 的发生。

在互联网大数据量，高并发量的场景下，几乎 **不会使用** 上述两种隔离级别。

 3.可重复读（Repeatable read）：

MySql默认隔离级别。

可避免 ***脏读*** 、***不可重复读*** 的发生。

4.串行化（Serializable ）：

可避免 ***脏读、不可重复读、幻读*** 的发生。

查询数据库的隔离级别：

``````mysql
select @@transaction_isolation;
``````



# (数据)模式

定义：也称逻辑模式，是数据库中全体数据的逻辑结构和特征的描述，是所有用户的公共数据视图。

* 外模式(External Schema)
  数据库用户(包括应用程序员和最终用户)能够看见和使用的局部数据的逻辑结构和特征的描述，是数据库用户的数据视图
* 内模式(Internal Schema)
  也称存储模式(Storage Schema)，它是数据物理结构和存储方式的描述，是数据在数据库内部的表示方式

# MYSQL存储引擎

MySQL支持多种存储引擎,比如InnoDB,MyISAM,Memory,Archive等等.在大多数的情况下,直接选择使用InnoDB引擎都是最合适的,InnoDB也是MySQL的默认存储引擎.

| 存储引擎的对比 |        |        |        |
| -------------- | ------ | ------ | ------ |
| 特性           | InnoDB | MyISAM | MEMORY |
| 事务安全       | 支持   | 无     | 无     |
| 存储限制       | 64TB   | 有     | 有     |
| 空间使用       | 高     | 低     | 低     |
| 内存使用       | 高     | 低     | 高     |
| 插入数据的速度 | 低     | 高     | 高     |
| 对外键的支持   | 支持   | 无     | 无     |

# 存储过程

存储过程（Stored Procedure）是在大型数据库系统中，一组为了完成特定功能的SQL
语句集，存储在数据库中，经过第一次编译后调用不需要再次编译，用户通过指定存储过程的名字并给出参数（如果该存储过程带有参数）来执行它。

* 触发器
  触发器是一种特殊类型的存储过程，它不同于存储过程。触发器主要是通过事件进行触发而被执行的，而存储过程可以通过存储过程名字而被直接调用。当对某一表进行诸如Update、Insert、Delete这些操作时，SQL Server 就会自动执行触发器所定义的SQL语句，从而确保对数据的处理必须符合由这些SQL语句所定义的规则。

# SQL注入

SQL注入，就是通过把SQL命令插入到Web表单递交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令，比如先前的很多影视网站泄露VIP会员密码大多就是通过WEB表单递交查询字符暴出的，这类表单特别容易受到SQL注入式攻击．

# 关键字

`INNER JOIN`
在表中存在至少一个匹配时，INNER JOIN 关键字返回行。(=JOIN)
`LEFT JOIN`
LEFT JOIN 关键字会从左表 (table_name1) 那里返回所有的行，即使在右表
(table_name2) 中没有匹配的行。
`natural join`
根据左右两表的**相同列**创建一个隐含的join操作，相同列就是两表中列名相同的两列。自然交可以是内交，左交或者是右交。默认是内交。
`Having`
"Having"是一个过滤声明，是在查询返回结果集以后对查询结果进行的过滤操作，在Having中可以使用聚合函数。

# RDBMS vs NoSQL

**RDBMS**(Relational Database Management System)
\- 高度组织化结构化数据
\- 结构化查询语言（SQL） (SQL)
\- 数据和关系都存储在单独的表中。
\- 数据操纵语言，数据定义语言
\- 严格的一致性
\- 基础事务

**NoSQL**(Not Only SQL)
\- 代表着不仅仅是SQL
\- 没有声明性查询语言
\- 没有预定义的模式
-键 - 值对存储，列存储，文档存储，图形数据库
\- 最终一致性，而非ACID属性
\- 非结构化和不可预知的数据
\- CAP定理
\- 高性能，高可用性和可伸缩性

# 常见的数据库调优

1.  选取合适的字段属性
2.  使用join代替子查询
3.  使用union代替创建临时表
4.  使用事务避免数据不完整的情况
5.  锁定表
6.  使用外键保证数据的关联性
7.  使用索引
8.  优化的查询语句

## 索引

1. 索引是一种数据结构,可以帮助我们快速的进行数据的查找.对数据库表中一列或多列的值进行排序的一种结构
   索引能让数据库查询数据的速度上升(SQL优化的范畴)，而使写入数据的速度下降。因为平衡树这个结构必须一直维持在一个正确的状态，增删改数据都会改变平衡树各节点中的索引数据内容，破坏树结构，因此，在每次数据改变时，DBMS必须去重新梳理树（索引）的结构以确保它的正确，这会带来不小的性能开销

2. 索引的数据结构和具体存储引擎的实现有关, 在MySQL中使用较多的索引有Hash索引,B+树索引等,而我们经常使用的InnoDB存储引擎的默认索引实现为:B+树索引.

# case

4张表：

``````mysql
CREATE TABLE `employees` (
`emp_no`  int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));
``````

``````mysql
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));
``````

``````mysql
CREATE TABLE `dept_manager` (
`dept_no` char(4) NOT NULL,
`emp_no` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
``````

``````mysql
CREATE TABLE `dept_emp` (
`emp_no` int(11) NOT NULL,
`dept_no` char(4) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
``````

1.  查找最晚入职员工的所有信息
    `select * from employees where hire_date = (select max(hire_date) from employees)`

2.  查找入职员工时间排名倒数第三的员工所有信息
    limit n,m: 从n+1行开始，共m行
    `select * from employees where hire_date = (select distinct hire_date from employees order by hire_date desc limit 2,1)`

3.  查找各个部门当前(to_date='9999-01-01')领导当前薪水详情以及其对应部门编号dept_no
    `select s.*,d.dept_no from salaries s,dept_manager d where s.to_date = '9999-01-01' and d.to_date = '9999-01-01' and s.emp_no = d.emp_no`

4.  查找所有已经分配部门的员工的last_name和first_name
    `SELECT e.last_name, e.first_name, d.dept_no FROM dept_emp d NATURAL JOIN employees e;`

5.  查找所有员工的last_name和first_name以及对应部门编号dept_no，也包括展示没有分配具体部门的员工
    `select e.last_name,e.first_name,d.dept_no from employees e left join dept_emp d on e.emp_no=d.emp_no`

6.  查找所有员工入职时候的薪水情况，给出emp_no以及salary，
    并按照emp_no进行逆序

-   方法1
    找出最小日期也可以说是最早的日期（
    min（from_date）），这个最小日期就是员工刚入职时候的日期，对应的工资就是入职时候的工资
    
    ``````mysql
    select emp_no,salary from salaries group by emp_no having min(from_date) order by emp_no DESC
    ``````
-   方法2 直接用逗号并列查询两张表
    `SELECT e.emp_no, s.salary FROM employees AS e, salaries AS s  WHERE e.emp_no = s.emp_no AND e.hire_date = s.from_date   ORDER BY e.emp_no DESC`

7.  查找薪水涨幅超过15次的员工号emp_no以及其对应的涨幅次数t

-   分析：
    1、用COUNT()函数和GROUP BY语句可以统计同一emp_no值的记录条数
    2、根据题意，输出的涨幅次数为t，故用AS语句将COUNT(emp_no)的值转换为t
    3、由于COUNT()函数不可用于WHERE语句中，故使用HAVING语句来限定t\>15的条件
    
    ``````mysql
    select emp_no, count(emp_no) as t FROM salaries GROUP BY emp_no HAVING t > 15
    ``````

8.  找出所有员工当前(to_date='9999-01-01')具体的薪水salary情况，对于相同的薪水只显示**一次**,并按照逆序显示

    1. `select salary from salaries  where to_date='9999-01-01' group by salary order by salary desc;`
    2. 

    ``````mysql
    select DISTINCT salary FROM salaries WHERE to_date = '9999-01-01' ORDER BY salary DESC;
    ``````

    在不同记录数较小时，count group by性能普遍高于count distinct

9.  获取所有部门当前manager的当前薪水情况，给出dept_no,
    emp_no以及salary，当前表示to_date='9999-01-01'
    `SELECT d.dept_no, d.emp_no, s.salary  FROM salaries AS s INNER JOIN dept_manager AS d ON d.emp_no = s.emp_no AND d.to_date = '9999-01-01' AND s.to_date = '9999-01-01'`

10. WITH ROLLUP
    可以实现在分组统计数据基础上再进行相同的统计（SUM,AVG,COUNT...）。
    如我们将以上的数据表按名字进行分组，再统计每个人登录的次数：
    SELECT name, SUM(singin) as singin_count FROM employee_tbl GROUP BY
    name WITH ROLLUP;

# 模型

* 按所使用的数据模型来分，数据库可分为三种模型:
  层次、关系和网状

关系模型中：
一个关键字是由一个或多个其值能惟一标识该关系模式中任何元组的属性组成

-   ER模型： 实体关系/联系模型\
    将实体-联系模型转换为关系模型时，实体之间多对多联系在关系模型中的实现方式是
    建立新的关键字
-   范式
    设计关系数据库时，遵从不同的规范要求，设计出合理的关系型数据库，这些不同的规范要求被称为不同的范式，各种范式呈递次规范，越高的范式数据库冗余越小。
-   封锁类型 排它锁(X锁)和共享锁(S锁)：
    所谓X锁,是事务T对数据A加上X锁时,只允许事务T读取和修改数据A
    所谓S锁,是事务T对数据A加上S锁时,其他事务只能再对数据A加S锁,而不能加X锁,直到T释放A上的S锁
-   数据库事务并发带来的问题 更新丢失、脏读、不可重复读、幻象读
-   DDBS
    数据按实际需要已在网络上分布存储，再采用集中式处理，势必造成通信开销大；应用程序集中在一台计算机上运行，一旦该计算机发生故障，则整个系统受到影响，可靠性不高；集中式处理引起系统的规模和配置都不够灵活，系统的可扩充性差。所以采用DDBS（分布式数据库系统）
-   数据库三级模式 外模式、概念模式、内模式
    数据的逻辑独立性：当模式发生改变时，只要改变其映射，就可以使外模式保持不变，对应的应用程序也可保持不变

# mysql binlog

binlog是二进制日志文件，用于记录mysql的数据更新或者潜在更新(比如DELETE语句执行删除而实际并没有符合条件的数据)，在mysql主从复制中就是依靠的binlog。

## 三种工作模式

Row level

Statement level

Mixed

> from
>  https://www.nowcoder.com/ta/sql
>  https://blog.csdn.net/Somhu/article/details/78775198
>  https://blog.csdn.net/qq_22222499/article/details/79060495
>
> https://blog.csdn.net/weixin_30661579/article/details/113723784
