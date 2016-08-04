#-*-coding:utf8-*-
import requests
import time
from uiautomator import device as d
import re
import os
import random

hongbaosuoping='462'
yaoqingmahongbaosuoping='12324'
kuhua='821'
kuhuayaoqingma='827155608'

def textclick(ctext):
    try:
        d(text=ctext).click()
    except:
        print 'textclick error:'+ctext
        print Exception

class kuhua(object):
    def __init__(self):
        print 'kuhua ...'

    def firstdo(self):
        try:
            #向右滑动解锁
            # d(resourceId='com.coohuaclient:id/tv_slide_horizontal_guide').drag.to(resourceId='com.coohuaclient:id/view_hand',steps=100)
            # textclick('点我左划试试')
            # d(resourceId='com.coohuaclient:id/tv_slide_horizontal_guide').drag.to(resourceId='com.coohuaclient:id/tv_left_cost',steps=100)
            # d(resourceId='com.coohuaclient:id/btn_click_me').click()
            # #上划
            # d(resourceId='com.coohuaclient:id/wave_circle_up').drag.to(d.info['displaySizeDpX']/2,100,steps=50)
            #d(resourceId='com.coohuaclient:id/wave_circle_down').drag.to(d.info['displaySizeDpX']/2,d.info['displaySizeDpY'],steps=50)

            #跳过
            d(resourceId='com.coohuaclient:id/tv_date').click()
            d(resourceId='com.coohuaclient:id/btn_register').click()
        except:
            print Exception

        try:
            textclick(u'注册')
        except:
            print Exception

    def requestVerfiyCode(self,phonenum):

        try:
            print "phonenum:" + phonenum
            d(resourceId='com.coohuaclient:id/et_phone_num').clear_text()
            d(resourceId='com.coohuaclient:id/et_phone_num').set_text(phonenum)
            textclick(u'获取验证码')
            time.sleep(2)
        except:
            print Exception

    def isPhoneRegisted(self):
        if  d(resourceId='com.coohuaclient:id/btn_get_verify_code').info['text']==u'获取验证码' :
            return True
        else:
            return False

    def fillVerifycode(self,verifycode):
        d(resourceId='com.coohuaclient:id/et_verify_code').set_text(verifycode)
        textclick(u'下一步')

    def continueRegiste(self):
        password = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(4)))
        print "password:" +password
        d(resourceId='com.coohuaclient:id/edt_password').set_text(password)
        d(resourceId='com.coohuaclient:id/edt_confirm_password').set_text(password)
        textclick(u'下一步')

        try:
            d(text=u'邀请人的酷划号/手机号').set_text(kuhuayaoqingma)
        except:
            print Exception
        d(resourceId='com.coohuaclient:id/rbn_male').click()
        d(resourceId='com.coohuaclient:id/edt_birth_year').click()
        textclick(u'确定')
        textclick(u'可以使用酷划了')
        textclick(u'设置完成')
        textclick(u'以后在“更多-设置”中设置')
        try:
            d(resourceId='com.coohuaclient:id/btn_later_set_in_settings').click()
        except:
            print Exception
        textclick(u'下一步')
        textclick(u'酷划商城')
        textclick(u'更多')
        textclick(u'我的账号')
        textclick(u'管理收货地址')
        return  password
