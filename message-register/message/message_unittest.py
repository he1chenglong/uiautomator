#-*-coding:utf8-*-
import requests
import time
from m51ym import m51ym
from uiautomator import device as d
import re
import os
import random
import sys
import unittest
reload(sys)
sys.setdefaultencoding("utf-8")

class TestMessage(unittest.TestCase):

    def setUp(self):
        print 'setup ...'

    def test_init(self):
        print u'test message __init__ ...'
        self.m=m51ym('821')

    def test_login(self):
        self.m.login()

    def test_getPhoneNumber(self):
        self.m.getPhoneNumber()

    def test_getVerifyCode(self):
        self.getVerifyCode()

    def test_releasePhoneNumber(self):
        self.m.releasePhoneNumber()

    def tearDown(self):
        print 'tearDown ...'

if __name__ == '__name__':
    unittest.main()
