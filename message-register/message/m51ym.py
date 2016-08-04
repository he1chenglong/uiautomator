#-*-coding:utf8-*-
import requests
import time
from uiautomator import device as d
import re
import os
import random
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class m51ym(object):
    def __init__(self,projectid):
        print u'messagebase __init__ ...projectid:'+projectid
        self.__pid=projectid
        # login(self)

    def login(self):
        self.__username='he1chenglong'
        self.__password='1qazsw2'
        #s=requests.get('http://api.51ym.me/UserInterface.aspx?action=login&username=he1chenglong&password=1qazsw2')
        # http://api.51ym.me/UserInterface.aspx?action=login&username=�û���&password=����
        cmd='http://api.51ym.me/UserInterface.aspx?action=login&username=%s&password=%s'%(self.__username,self.__password)
        s=requests.get(cmd)
        print 'login  gettoken:'
        print s.text
        l=s.text.split("|")
        self.__token= l[1]

    def getPhoneNumber(self):
        # http://api.51ym.me/UserInterface.aspx?action=getmobile&itemid=��Ŀ���&token=token
        cmd='http://api.51ym.me/UserInterface.aspx?action=getmobile&itemid=%s&token=%s'%(self.__pid,self.__token)
        pn=requests.get(cmd)
        print 'getPhoneNumber:'
        print pn.text
        li=pn.text.split("|")
        self.__pnum = li[1]
        return li[1]

    def readPhoneNum(self):
        return self.__pnum

    def releasePhoneNumber(self):
        #http://api.51ym.me/UserInterface.aspx?action=release&mobile=�绰����&itemid=��Ŀ���&token=token
        cmd='http://api.51ym.me/UserInterface.aspx?action=release&mobile=%s&itemid=%s&token=%s'%(self.__pnum,self.__pid,self.__token)
        ret=requests.get(cmd)
        print 'releasePhoneNumber '+ ret.text

    def phoneBlacklist(self):
        #http://api.51ym.me/UserInterface.aspx?action=addignore&mobile=�绰����&itemid=��Ŀ���&token=token
        cmd='http://api.51ym.me/UserInterface.aspx?action=addignore&mobile=%s&itemid=%s&token=%s'%(self.__pnum,self.__pid,self.__token)
        ret=requests.get(cmd)
        print 'phoneBlacklist '+ret.text

    def getVerifyCode(self):
        # http://api.51ym.me/UserInterface.aspx?action=getsms&mobile=�绰����&itemid=��Ŀ���&token=token
        for i in range(0,50):
            cmd='http://api.51ym.me/UserInterface.aspx?action=getsms&mobile=%s&itemid=%s&token=%s'%(self.__pnum,self.__pid,self.__token)
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

    # def releasePhoneNumber(self,num):
    #     #http://api.51ym.me/UserInterface.aspx?action=release&mobile=�绰����&itemid=��Ŀ���&token=token
    #     cmd='http://api.51ym.me/UserInterface.aspx?action=release&mobile=%s&itemid=%s&token=%s'%(num,self.__pid,self.__token)
    #     ret=requests.get(cmd)
    #     print 'releasePhoneNumber '+ ret.txt
    #
    # def phoneBlacklist(self,num):
    #     #releasePhoneNumber(self,num)
    #     #http://api.51ym.me/UserInterface.aspx?action=addignore&mobile=�绰����&itemid=��Ŀ���&token=token
    #     cmd='http://api.51ym.me/UserInterface.aspx?action=addignore&mobile=%s&itemid=%s&token=%s'%(num,self.__pid,self.__token)
    #     ret=requests.get(cmd)
    #     print 'blacklist '+ret.txt
    #
    # def getVerifyCode(self,num):
    #     # http://api.51ym.me/UserInterface.aspx?action=getsms&mobile=�绰����&itemid=��Ŀ���&token=token
    #     for i in range(0,50):
    #         cmd='http://api.51ym.me/UserInterface.aspx?action=getsms&mobile=%s&itemid=%s&token=%s'%(num,self.__pid,self.__token)
    #         vc=requests.get(cmd)
    #         print vc.text
    #         if vc.text[0:7] == 'success':
    #             print 'try to find the number:'
    #             numlist=re.findall('(\d+)',vc.text,re.S)
    #             print 'getVerifyCode:'+numlist[0]
    #             return numlist[0]
    #         else:
    #             time.sleep(5)
    #
    #     return '0000'

if __name__ =='__main__':
    m=message('821')
    m.login()
    m.getPhoneNumber()