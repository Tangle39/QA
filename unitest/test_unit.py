#coding=utf-8
'''
单元测试
https://www.bilibili.com/video/av19430527/?p=9&t=1789
'''
from count import Count #后面一个是类，前一个是文件
import true_f
import unittest #单元测试框架

class TestCount(unittest.TestCase):
    def setUp(self):
        self.j = Count(2,3)
    def test_add(self):   #测试用例，必须以test开头
        self.add = self.j.add()
        self.assertEqual(self.add,5)
        #assert断言  | https://www.cnblogs.com/feiyueNotes/p/7788995.html，unittest提供了许多assert方法
    #def test_add2(self):
    #     self.add = self.j.add()
    #     self.assertEqual(self.add,5.0)
    def test_true(self):
        self.prime =true_f.is_prime(2)
        self.assertTrue(self.prime,msg='Is not prime~です')

    def tearDown(self):
        pass
# tearDown：清理工作| https://www.cnblogs.com/insane-Mr-Li/p/9085062.html


if __name__ == '__main__':
    unittest.main()
# 如何简单地理解Python中的if __name__ == '__main__'
# https://blog.csdn.net/yjk13703623757/article/details/77918633

    #运行所有的testcase

'''   suite = unittest.TestSuite()
    suite.addTest(TestCount('test_true'))
#执行单个测试
    runner=unittest.TextTestRunner()
    runner.run(suite)
'''