# coding=utf-8

## 01

# import sys
#
# sys.path.append("/home/lynxi/PycharmProjects/flaskdemo/pytest/")
#
# import unittest
# from UnittestCase.test_case01 import TestCase01
# from UnittestCase.test_case02 import TestCase02
#
# case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
#
# suote = unittest.TestSuite([case_01, case_02])
# unittest.TextTestRunner().run(suote)

## 02
import sys
import os
import unittest
# case_path = os.getcwd() + "/UnittestCase/"
case_path = os.getcwd()
print(case_path)

discovery = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discovery)

print(discovery)
