# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest
import test_baidu
import test_youdao

#构造测试集
suite = unittest.TestSuite()
suite.addTest(test_baidu.BaiduTest('test_baidu0'))
suite.addTest(test_youdao.YoudaoTest('test_youdao'))

if __name__=='__main__':
    #执行测试
    # 单元测试时一般不直接使用 TestRunner 类，而是使用其子类 TextTestRunner 来完成测试，
    # 并将测试结果以文本方式显示出来：

    runner = unittest.TextTestRunner()
    runner.run(suite)