# 事务(Transaction)四大特性  
原子性，要么执行，要么不执行  
隔离性，所有操作全部执行完以前其它会话不能看到过程  
一致性，事务前后，数据总额一致  
持久性，一旦事务提交，对数据的改变就是永久的  

# (数据)模式  
定义：也称逻辑模式，是数据库中全体数据的逻辑结构和特征的描述，是所有用户的公共数据视图。  
* 外模式(External Schema)  
数据库用户(包括应用程序员和最终用户)能够看见和使用的局部数据的逻辑结构和特征的描述，是数据库用户的数据视图  
* 内模式(Internal Schema)  
也称存储模式(Storage Schema)，它是数据物理结构和存储方式的描述，是数据在数据库内部的表示方式  

# 数据库隔离级别  
脏读(Read out of invalid data)：事务B读取事务A还没有提交的数据  
不可重复读：两次事务读的数据不一致（事务A首先读取了一条数据，然后执行逻辑的时候，事务B将这条数据改变了，然后事务A再次读取的时候，发现数据不匹配了，就是所谓的不可重复读了）  
幻读:事务A修改了数据，事务B也修改了数据，这时在事务A看来，明明修改了数据，咋不一样  

# MYSQL的两种存储引擎  

<table>
<thead>
<tr>
<th>引擎</th>
<th>特性</th>
</tr>
</thead>
<tbody>
<tr>
<td>MYISAM</td>
<td>不支持外键，表锁，插入数据时，锁定整个表，查表总行数时，不需要全表扫描</td>
</tr>
<tr>
<td>INNODB</td>
<td>支持外键，行锁，查表总行数时，全表扫描</td>
</tr>
</tbody>
</table>  

# 索引  
索引是对数据库表中一列或多列的值进行排序的一种结构  
索引能让数据库查询数据的速度上升(SQL优化的范畴)，而使写入数据的速度下降，原因很简单的，因为平衡树这个结构必须一直维持在一个正确的状态，增删改数据都会改变平衡树各节点中的索引数据内容，破坏树结构，因此，在每次数据改变时， DBMS必须去重新梳理树（索引）的结构以确保它的正确，这会带来不小的性能开销  

# 存储过程
存储过程（Stored Procedure）是在大型数据库系统中，一组为了完成特定功能的SQL 语句集，存储在数据库中，经过第一次编译后调用不需要再次编译，用户通过指定存储过程的名字并给出参数（如果该存储过程带有参数）来执行它。  
* 触发器  
触发器是一种特殊类型的存储过程，它不同于存储过程。触发器主要是通过事件进行触发而被执行的，而存储过程可以通过存储过程名字而被直接调用。当对某一表进行诸如Update、Insert、Delete这些操作时，SQL Server 就会自动执行触发器所定义的SQL语句，从而确保对数据的处理必须符合由这些SQL语句所定义的规则。  

# SQL注入  
SQL注入，就是通过把SQL命令插入到Web表单递交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令，比如先前的很多影视网站泄露VIP会员密码大多就是通过WEB表单递交查询字符暴出的，这类表单特别容易受到SQL注入式攻击．  

# 关键字  
INNER JOIN  
在表中存在至少一个匹配时，INNER JOIN 关键字返回行。(=JOIN)
LEFT JOIN   
LEFT JOIN 关键字会从左表 (table_name1) 那里返回所有的行，即使在右表 (table_name2) 中没有匹配的行。  
natural join  
根据左右两表的**相同列**创建一个隐含的join操作，相同列就是两表中列名相同的两列。自然交可以是内交，左交或者是右交。默认是内交。   
Having  
“Having”是一个过滤声明，是在查询返回结果集以后对查询结果进行的过滤操作，在Having中可以使用聚合函数。  

#常见的数据库调优
1. 选取

# case  
CREATE TABLE \`employees\` (  
\`emp_no\` int(11) NOT NULL,  
`birth_date` date NOT NULL,  
`first_name` varchar(14) NOT NULL,    
`last_name` varchar(16) NOT NULL,  
`gender` char(1) NOT NULL,  
`hire_date` date NOT NULL,  
PRIMARY KEY (`emp_no`));  

CREATE TABLE \`salaries\` (  
`emp_no` int(11) NOT NULL,  
`salary` int(11) NOT NULL,  
`from_date` date NOT NULL,  
`to_date` date NOT NULL,  
PRIMARY KEY (`emp_no`,`from_date`));    
CREATE TABLE `dept_manager` (  
`dept_no` char(4) NOT NULL,  
`emp_no` int(11) NOT NULL,  
`from_date` date NOT NULL,  
`to_date` date NOT NULL,  
PRIMARY KEY (`emp_no`,`dept_no`));  

CREATE TABLE \`dept_emp\` (  
`emp_no` int(11) NOT NULL,  
`dept_no` char(4) NOT NULL,   
`from_date` date NOT NULL,    
`to_date` date NOT NULL,  
PRIMARY KEY (`emp_no`,`dept_no`));  




1. 查找最晚入职员工的所有信息  
`select * from employees where hire_date = (select max(hire_date) from employees)`  
2. 查找入职员工时间排名倒数第三的员工所有信息  
limit n,m: 从n+1行开始，共m行  
`select * from employees where hire_date = (select distinct hire_date from employees order by hire_date desc limit 2,1)`  
3. 查找各个部门当前(to_date='9999-01-01')领导当前薪水详情以及其对应部门编号dept_no  
`select s.*,d.dept_no from salaries s,dept_manager d where s.to_date = '9999-01-01' and d.to_date = '9999-01-01' and s.emp_no = d.emp_no`  
4. 查找所有已经分配部门的员工的last_name和first_name  
`SELECT e.last_name, e.first_name, d.dept_no
FROM dept_emp d NATURAL JOIN employees e;`  
5. 查找所有员工的last_name和first_name以及对应部门编号dept_no，也包括展示没有分配具体部门的员工  
`select e.last_name,e.first_name,d.dept_no 
from employees e left join dept_emp d on e.emp_no=d.emp_no`  
6. 查找所有员工入职时候的薪水情况，给出emp_no以及salary， 并按照emp_no进行逆序  
* 方法1  
找出最小日期也可以说是最早的日期（ min（from_date）），这个最小日期就是员工刚入职时候的日期，对应的工资就是入职时候的工资  
`select emp_no,salary from salaries group by emp_no having min(from_date) order by emp_no DESC`  
* 方法2
直接用逗号并列查询两张表  
`SELECT e.emp_no, s.salary FROM employees AS e, salaries AS s  
WHERE e.emp_no = s.emp_no AND e.hire_date = s.from_date  
ORDER BY e.emp_no DESC`  
7. 查找薪水涨幅超过15次的员工号emp_no以及其对应的涨幅次数t  
* 分析：  
1、用COUNT()函数和GROUP BY语句可以统计同一emp_no值的记录条数  
2、根据题意，输出的涨幅次数为t，故用AS语句将COUNT(emp_no)的值转换为t  
3、由于COUNT()函数不可用于WHERE语句中，故使用HAVING语句来限定t>15的条件  
`select emp_no, count(emp_no) as t FROM salaries GROUP BY emp_no HAVING t > 15`  
8. 找出所有员工当前(to_date='9999-01-01')具体的薪水salary情况，对于相同的薪水只显示一次,并按照逆序显示  
`1. select salary from salaries  where to_date='9999-01-01' group by salary order by salary desc;`  
`2. SELECT DISTINCT salary FROM salaries WHERE to_date = '9999-01-01' ORDER BY salary DESC`  
在不同记录数较小时，count group by性能普遍高于count distinct

>from  
https://www.nowcoder.com/ta/sql  
https://blog.csdn.net/Somhu/article/details/78775198  
https://blog.csdn.net/qq_22222499/article/details/79060495#1_4
