# 事务(Transaction)四大特性  
原子性，要么执行，要么不执行  
隔离性，所有操作全部执行完以前其它会话不能看到过程  
一致性，事务前后，数据总额一致  
持久性，一旦事务提交，对数据的改变就是永久的  
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

# 关键字  
## INNER JOIN  
在表中存在至少一个匹配时，INNER JOIN 关键字返回行。(=JOIN)
## SQL LEFT JOIN 关键字  
LEFT JOIN 关键字会从左表 (table_name1) 那里返回所有的行，即使在右表 (table_name2) 中没有匹配的行。  
# SQL注入  
SQL注入，就是通过把SQL命令插入到Web表单递交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令，比如先前的很多影视网站泄露VIP会员密码大多就是通过WEB表单递交查询字符暴出的，这类表单特别容易受到SQL注入式攻击．  
## case  
CREATE TABLE \`employees\` (  
\`emp_no\` int(11) NOT NULL,  
`birth_date` date NOT NULL,  
`first_name` varchar(14) NOT NULL,    
`last_name` varchar(16) NOT NULL,  
`gender` char(1) NOT NULL,  
`hire_date` date NOT NULL,  
PRIMARY KEY (`emp_no`));  

CREATE TABLE `salaries` (  
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

?1. 查找所有员工入职时候的薪水情况，给出emp_no以及salary， 并按照emp_no进行逆序  
* 方法1  
找出最小日期也可以说是最早的日期（ min（from_date）），这个最小日期就是员工刚入职时候的日期，对应的工资就是入职时候的工资  
`select emp_no,salary from salaries group by emp_no having min(from_date) order by emp_no DESC`  
* 方法2
直接用逗号并列查询两张表  
`SELECT e.emp_no, s.salary FROM employees AS e, salaries AS s  
WHERE e.emp_no = s.emp_no AND e.hire_date = s.from_date  
ORDER BY e.emp_no DESC`  
?2. 查找薪水涨幅超过15次的员工号emp_no以及其对应的涨幅次数t  
* 分析：
1、用COUNT()函数和GROUP BY语句可以统计同一emp_no值的记录条数  
2、根据题意，输出的涨幅次数为t，故用AS语句将COUNT(emp_no)的值转换为t  
3、由于COUNT()函数不可用于WHERE语句中，故使用HAVING语句来限定t>15的条件  
`select emp_no, count(emp_no) as t FROM salaries GROUP BY emp_no HAVING t > 15`

1. 查找最晚入职员工的所有信息
select * from employees where hire_date = (select max(hire_date) from employees)  
2. 查找入职员工时间排名倒数第三的员工所有信息  
`select * from employees where hire_date = (select distinct hire_date from employees order by hire_date desc limit 2,1)`  
3. 查找各个部门当前(to_date='9999-01-01')领导当前薪水详情以及其对应部门编号dept_no  
`select s.*,d.dept_no from salaries s,dept_manager d where s.to_date = '9999-01-01' and d.to_date = '9999-01-01' and s.emp_no = d.emp_no`

>from  
https://www.nowcoder.com/ta/sql  
https://blog.csdn.net/Somhu/article/details/78775198  
https://blog.csdn.net/qq_22222499/article/details/79060495#1_4
