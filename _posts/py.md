# 人生苦短，我用python
1. tuple与list
tuple一旦初始化就不能修改，而且没有append() insert()这些方法，可以获取元素但不能赋值变成另外的元素  
2. 装了py3，现在电脑里同时有py2，py3如何装第三方库？  
[python3 pip install pandas  
安装flask时需要直接pip install成功 晕]  
pip3 install **
3. python -m xxx.py？  
相当于import,叫做当做模块来启动  
4. py2和py3的区别  
* py2:  
（1）源码重复量多，臃肿。  
（2）源码语法不清晰，掺杂着c,php,java的一些陋习  
py3:几乎是重构后的源码，规范，清晰，优美  
* py2:默认ASKLL编码不能识别中文。文件头需要添加：#-- encoding:utf-8 --  
  py3:默认编码方式就是utf-8  
* 输入输出  
* Unicode 字符串：在Python3中，所有的字符串都是Unicode字符串。  
   py2：在字符串前面加上前缀 u  
* Python 3.x已经改进了整数的除法运算，“/”除将得到浮点数，“//”除才仍是整数。
* py3的一些函数的返回类型是迭代器，如reversed
5. pycharm优化代码格式：
Code→Reformmat code（快捷键option+command+L）
6. \*args 和 \*\*kwargs
其实并不是必须写成\*args 和\*\*kwargs。 只有变量前面的 \*(星号)才是必须的. 你也可以写成\*var 和\*\*vars. 而写成\*args 和\*\*kwargs只是一个通俗的命名约定。  
主要用于函数定义。 你可以将不定数量的参数传递给一个函数。  
7. 调试
* 命令行运行
python -m pdb my_script.py  
* c: 继续执行
* w: 显示当前正在执行的代码行的上下文信息
* a: 打印当前函数的参数列表
* s: 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
* n: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）

0901
* 字典
字典中键必须是唯一的。列表中的项目包括在方括号中。列表是可变的数据类型（可以增加或删除项目）。所以，列表中的项目不能用来作为字典的键。

* open
r:只读模式
w:写（覆盖写）
a:追加模式
b:二进制格式

* 前导r
Python 中字符串的前导 r 代表原始字符串标识符，该字符串中的特殊符号不会被转义