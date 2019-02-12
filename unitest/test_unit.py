#coding=utf-8
'''
单元测试
https://www.bilibili.com/video/av19430527/?p=9&t=1789
'''
from count import Count #后面一个是类，前一个是文件
import unittest #单元测试框架

class TestCount(unittest.TestCase):
    def setUp(self):
        self.j = Count(2,3)
    def test_add(self):   #必须以test开头
        self.add = self.j.add()
        self.assertEqual(self.add,5)
        #assert断言  | https://www.cnblogs.com/feiyueNotes/p/7788995.html

    def tearDown(self):
        pass
# tearDown：清理工作| https://www.cnblogs.com/insane-Mr-Li/p/9085062.html


if __name__ == '__main__':
    unittest.main()