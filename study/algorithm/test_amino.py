import unittest
import amino


class TestAmino(unittest.TestCase):
    def setUp(self):
        pass

    def test_conver_ip(self):
        ip = '17 2.168.5.1'
        self.con_ip = amino.conver_ip(ip)
        self.assertEqual(self.con_ip, 'error!')

    def test_conver_ip1(self):
        ip = '172.168.5.1'
        self.con_ip = amino.conver_ip(ip)
        self.assertEqual(self.con_ip, 2896692481)

    def test_conver_ip2(self):
        ip = ' 172 . 168 . 5 .1'
        self.con_ip = amino.conver_ip(ip)
        self.assertEqual(self.con_ip, 2896692481)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
