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

hongbaosuoping='462'
yaoqingmahongbaosuoping='12324'
kuhuapid='821'
kuhuayaoqingma='827155608'

if __name__ == '__main__':

    logfile=file("phone_num_kuhua.txt","a+")

    device= deviceinfo()
    device.changeDeviceInfoRealtool()
    device.changeDeviceInfo008()

    kuhua=kuhua()
    kuhua.firstdo()

    projectId=kuhuapid
    mes=m51ym(projectId)
    mes.login()
    pnum=mes.getPhoneNumber()

    kuhua.requestVerfiyCode(pnum)

    for i in range(0,30):
        if  kuhua.isPhoneRegisted() :
            print pnum+' 已经被注册过了'
            logfile.write(pnum+' 已经被注册过了 \n')
            mes.phoneBlacklist()
            mes.releasePhoneNumber()
            pnum=mes.getPhoneNumber()
            mes.requestVerfiyCode(pnum)
        else:
            vcode=mes.getVerifyCode()
            if vcode != '0000':
                break


    kuhua.fillVerifycode(vcode)
    passw = kuhua.continueRegiste()
    logfile.write('register '+pnum+'  '+passw+'\n')

    logfile.close()
    mes.releasePhoneNumber(pnum,projectId)





