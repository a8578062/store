import unittest
from homework.jiatest import TestAdd
from homework.jiantest import TestIncre
from homework.chengtest import TestMulti
from homework.chutest import TestDevide

from HTMLTestRunner import HTMLTestRunner
import os
suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(os.getcwd(),"*test.py")
suite.addTest(tests)

f = open("计算器的测试报告.html","w+",encoding="utf-8") # 准备一个报告文件
runner = HTMLTestRunner.HTMLTestRunner(  # 使用html运行器写入到报告里
    stream = f, # 将报告写到那个文件流
    verbosity=1, # 报告的详细程度
    title="计算器的测试报告"
)
runner.run(suite)