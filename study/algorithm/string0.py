# -*-coding:utf8 -*-
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，
字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''


# float() 函数用于将整数和字符串转换成浮点数。
def isNumeric(s):
    try:
        p = float(s)
        return True
    except:
        return False


s = raw_input('字符串を输入ください\n')  # 输入字符串
print isNumeric(s)
