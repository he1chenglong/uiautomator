#-*-coding:utf8-*-
import requests
import time
from uiautomator import device as d
import re
import os
import random
import subprocess

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
        '''
        第一次打开，初始化008 神器
        :return:
        '''
        d.press.home()
        #textclick(u"008神器0113")
        subprocess.Popen('adb shell am start -n com.soft.apk008v/com.soft.apk008.LoadActivity')
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
        '''
        通过 008 神器更改设备信息
        :return:
        '''
        d.press.home()
        #textclick(u'008神器0113')
        subprocess.Popen('adb shell am start -n com.soft.apk008v/com.soft.apk008.LoadActivity')
        textclick(u'工具箱')
        textclick(u'快捷操作')
        #textclick(u'数据清除')
        textclick(u'一键操作')
        time.sleep(10)
        print 'change devcie info finish'

    def changeDeviceInfoRealtool(self):
        '''
        通过 realtool  更改设备信息
        :return:
        '''
        d.press.home()
        #textclick(u"ID：pc0123")
        subprocess.Popen('adb shell am start -n com.example.myxposed/.ParamActivity')
        textclick(u'随机并保存')

    def changeIp(self):
        '''
        换IP
        :return:
        '''
        d.press.home()
        textclick(u'无极VPN')

    def startApp(self,packageActivity):
        '''
        打开app
        :param packageActivity:
        :return:
        '''
        cmd = 'adb shell am start -n %s'%(packageActivity)
        subprocess.Popen(cmd)

    def startApp(self,packageName,activityName):
        '''
        打开app
        :param packageName: 包名
        :param activityName: activity 名
        :return:
        '''
        cmd = 'adb shell am start -n %s/.%s'%(packageName,activityName)
        subprocess.Popen(cmd)

    def installApp(self,appPatch):
        '''
        安装app
        :param appPatch:
        :return:
        '''
        cmd = 'adb install %s'%(appPatch)
        subprocess.Popen(cmd)

    def unstallApp(self,packageName):
        '''
        卸载app
        :param packageName:
        :return:
        '''
        cmd = 'adb shell pm uninstall %s'%(packageName)
        subprocess.Popen(cmd)

    def closeApp(self,packageName):
        '''
        关闭app
        :param packageName:
        :return:
        '''
        cmd = 'adb shell am force-stop %s'%(packageName)
        subprocess.Popen(cmd)

    def clearApp(self,packgaeName):
        '''
        清楚app 数据
        :param packgaeName:
        :return:
        '''
        cmd = 'adb shell pm clear %s'%(packgaeName)
        subprocess.Popen(cmd)
