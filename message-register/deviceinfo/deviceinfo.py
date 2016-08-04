#-*-coding:utf8-*-
import requests
import time
from uiautomator import device as d
import re
import os
import random

def textclick(ctext):
    try:
        d(text=ctext).click()
    except:
        print 'textclick error:'+ctext
        print Exception

class deviceinfo(object):
    def __init__(self):
        print 'device info ...'

    def init008(self):
        d.press.home()
        textclick(u"008神器0113")
        textclick(u'工具箱')
        textclick(u'快捷操作')
        textclick(u'设置应用')
        textclick(u'红包锁屏')
        for i in range(0,6):
            try:
                d(className='android.widget.CheckBox')[i].click()
            except:
                print Exception

        textclick(u'一键操作')
        time.sleep(5)

    def changeDeviceInfo008(self):
        d.press.home()
        textclick(u'008神器0113')
        #textclick(u'数据清除')
        textclick(u'一键操作')
        time.sleep(5)
        print 'change devcie info finish'

    def changeDeviceInfoRealtool(self):
        d.press.home()
        textclick(u"ID：pc0123")
        textclick(u'随机并保存')

    def changeIp(self):
        d.press.home()
        textclick(u'无极VPN')