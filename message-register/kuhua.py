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

def init008():
    d.press.home()
    textclick(u'008神器0113')
    textclick(u'工具箱')
    textclick(u'快捷操作')
    textclick(u'设置应用')
    textclick(u'红包锁屏')
    for i in range(0,6):
        d(className='android.widget.CheckBox')[i].click()
    textclick(u'一键操作')
    time.sleep(5)

def changeDeviceInfo008():
    d.press.home()
    textclick(u'008神器0113')
    textclick(u'清除')
    textclick(u'一键操作')
    time.sleep(5)
    print 'change devcie info finish'

def changeDeviceInfoRealtool():
    d.press.home()
    textclick(u"ID：pc0123")
    textclick(u'随机并保存')

def login():
    s=requests.get('http://api.51ym.me/UserInterface.aspx?action=login&username=he1chenglong&password=1qazsw2')
    print 'login  gettoken:'
    print s.text
    l=s.text.split("|")
    return l[1]

def getPhoneNumber(pid,token):
    # http://api.51ym.me/UserInterface.aspx?action=getmobile&itemid=项目编号&token=token
    cmd='http://api.51ym.me/UserInterface.aspx?action=getmobile&itemid=%s&token=%s'%(pid,token)
    pn=requests.get(cmd)
    print 'getPhoneNumber:'
    print pn.text
    li=pn.text.split("|")
    return li[1]

def releasePhoneNumber(num,pid,token):
    #http://api.51ym.me/UserInterface.aspx?action=release&mobile=电话号码&itemid=项目编号&token=token
    cmd='http://api.51ym.me/UserInterface.aspx?action=release&mobile=%s&itemid=%s&token=%s'%(num,pid,token)
    ret=requests.get(cmd)
    print 'releasePhoneNumber '+ ret.txt

def blacklist(num,pid,token):
    releasePhoneNumber(num,pid,token)
    #http://api.51ym.me/UserInterface.aspx?action=addignore&mobile=电话号码&itemid=项目编号&token=token
    cmd='http://api.51ym.me/UserInterface.aspx?action=addignore&mobile=%s&itemid=%s&token=%s'%(num,pid,token)
    ret=requests.get(cmd)
    print 'blacklist '+ret.txt

def getVerifyCode(phonenumber,projectid,token):
    # http://api.51ym.me/UserInterface.aspx?action=getsms&mobile=电话号码&itemid=项目编号&token=token
    for i in range(0,50):
        cmd='http://api.51ym.me/UserInterface.aspx?action=getsms&mobile=%s&itemid=%s&token=%s'%(phonenumber,projectid,token)
        vc=requests.get(cmd)
        print vc.text
        if vc.text[0:7] == 'success':
            print 'try to find the number:'
            numlist=re.findall('(\d+)',vc.text,re.S)
            print 'getVerifyCode:'+numlist[0]
            return numlist[0]
        else:
            time.sleep(5)

    return '0000'

def firstdo():
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

def requestVerfiyCode(phonenum):

    try:
        print "phonenum:" + phonenum
        d(resourceId='com.coohuaclient:id/et_phone_num').clear_text()
        d(resourceId='com.coohuaclient:id/et_phone_num').set_text(phonenum)
        textclick(u'获取验证码')
        time.sleep(2)
    except:
        print Exception


def fillVerifycode(verifycode):
    d(resourceId='com.coohuaclient:id/et_verify_code').set_text(verifycode)
    textclick(u'下一步')

def continueRegiste():
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


def main():
    print 'start test ...'
    changeDeviceInfoRealtool()
    #init008()
    logfile=file("phone_num_kuhua.txt","a+")
    changeDeviceInfo008()
    firstdo()

    token=login()
    projectId =kuhua
    pnum=getPhoneNumber(projectId,token)
    requestVerfiyCode(pnum)

    for i in range(0,30):
        if  d(resourceId='com.coohuaclient:id/btn_get_verify_code').info['text']==u'获取验证码' :
            print pnum+' 已经被注册过了'
            logfile.write(pnum+' 已经被注册过了 \n')
            blacklist(pnum,projectId,token)
            pnum=getPhoneNumber(projectId,token)
            requestVerfiyCode(pnum)
        else:
            vcode=getVerifyCode(pnum,projectId,token)
            if vcode != '0000':
                break


    fillVerifycode(vcode)
    passw = continueRegiste()
    logfile.write('register '+pnum+'  '+passw+'\n')

    logfile.close()
    releasePhoneNumber(pnum,projectId,token)

if __name__ == '__main__':
    main()