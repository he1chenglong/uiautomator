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

def init008():
    d.press.home()
    d(text=u'008神器0113').click()
    d(text=u'工具箱').click()
    d(text=u'快捷操作').click()
    d(text=u'设置应用').click()
    d(text=u'红包锁屏').click()
    for i in range(0,6):
        d(className='android.widget.CheckBox')[i].click()
    d(text=u'一键操作').click()

def changeDeviceInfo008():
    d.press.home()
    d(text=u'008神器0113').click()
    d(text=u'一键操作').click()

def login():
    s=requests.get('http://api.51ym.me/UserInterface.aspx?action=login&username=he1chenglong&password=1qazsw2')
    print 'login  gettoken:'
    print s.text
    l=s.text.split("|");
    return l[1]

def getPhoneNumber(pid,token):
    # http://api.51ym.me/UserInterface.aspx?action=getmobile&itemid=项目编号&token=token
    cmd='http://api.51ym.me/UserInterface.aspx?action=getmobile&itemid=%s&token=%s'%(pid,token)
    pn=requests.get(cmd)
    print 'getPhoneNumber:'
    print pn.text
    li=pn.text.split("|")
    return li[1]

def getVerifyCode(phonenumber,projectid,token):
    # http://api.51ym.me/UserInterface.aspx?action=getsms&mobile=电话号码&itemid=项目编号&token=token
    for i in range(0,15):
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


def requestVerfiyCode(phonenum):
    try:
        # d.press.home()
        # d(text=u'红包锁屏').click()
        try:
            d(text=u'输入邀请码').click()
            d(text=u'立即开始').click()
        except:
            print Exception
        d(text=u'我的').click()
        d(text=u'注册').click()
        # d(className='android.widget.EditText').clear_text()
        print "phonenum:" + phonenum
        d(className='android.widget.EditText').set_text(phonenum)
        d(text=u'获取验证码').click()
    except:
        print Exception


def continueRegiste(verifycode):
    d(className='android.widget.EditText')[0].set_text(verifycode[0])
    d(className='android.widget.EditText')[1].set_text(verifycode[1])
    d(className='android.widget.EditText')[2].set_text(verifycode[2])
    d(className='android.widget.EditText')[3].set_text(verifycode[3])
    #d(text=u'下一步').click()
    #password=''.join(random.sample(string.ascii_letters+string.digits, 8))
    password = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(4)))
    print "password:" +password
    d(className='android.widget.EditText').set_text('421768')
    d(text=u'确定').click()

def main():
    #init008()
    changeDeviceInfo008()
    token=login()
    projectId =hongbaosuoping
    pnum=getPhoneNumber(projectId,token)
    requestVerfiyCode(pnum)
    vcode=getVerifyCode(pnum,projectId,token)
    continueRegiste(vcode)


if __name__ == '__main__':
    main()