# coding=utf-8
import requests
import unittest

# data = {
#     "username": "ck",
#     "password": "111111"
# }


class TestCase02(unittest.TestCase):
    def setUp(self):
        print("case run begin!")

    def tearDown(self):
        print("case run end!")

    @classmethod
    def setUpClass(cls):
        print("case class run begin!!!")

    @classmethod
    def tearDownClass(cls):
        print("case class run end!!!")

    def test_01(self):
        print("case01")

    def test_02(self):
        print("case02")
        data1 = {
            "username": "ck",
            "password": "111111"
        }

        # self.assertDictEqual(data, data1, msg="this two dict is not equal")

    def test_03(self):
        print("case03")

    def test_04(self):
        print("case04")
        flag = False
        self.assertTrue(flag, msg="this two flag is not equal")

    def test_05(self):
        print("case05")
        flag = "111"
        flag1 = "2222"
        self.assertTrue(flag, flag1)

    @unittest.skipIf(4 < 5, "this case not execute")
    def test_06(self):
        print("case06")
        flag = "adfadfadfafdfadsfaqeewr"
        s = "fads"
        self.assertIn(s, flag, msg="this two string is not in")


if __name__ == '__main__':
    # unittest.main()
    
    suite = unittest.TestSuite()
    # suite.addTest(TestCase02('test_06'))
    # suite.addTest(TestCase02('test_05'))

    tests = [TestCase02("test_05"), TestCase02("test_06")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
