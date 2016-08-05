#-*-coding:utf8-*-
import requests
import time
from uiautomator import device as d
import re
import os
import random
from   deviceinfo.deviceinfo  import deviceinfo
from   appclick.kuhuaapp import kuhua
from   message.m51ym import m51ym

if __name__ == '__main__':
    '''
    测试app 时  取验证码信息
    '''
    mes=m51ym()
    mes.login()
    pnum=mes.getPhoneNumber()
    print "pnum is :" +pnum

    time.sleep(15)

    vcode=mes.getVerifyCode()
    print "verifycode is :" +vcode


    #mes.releasePhoneNumber(pnum)





