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

    logfile=file("phone_num_kuhua.txt","a+")

    # 更改设备信息
    device= deviceinfo()
    # 使用realtool 工具  更改设备信息
    device.changeDeviceInfoRealtool()
    #使用 008 神器 更改设备信息
    device.changeDeviceInfo008()

    #打开 app
    kuhua=kuhua()
    # app 初始化操作 到  填写手机号 的注册界面
    kuhua.firstdo()

    #  登陆验证码平台
    mes=m51ym()
    mes.login()
    # 获取 要注册 的手机号
    pnum=mes.getPhoneNumber()

    # 填写要注册的手机号  ，点击 获取验证码 按钮
    kuhua.requestVerfiyCode(pnum)

    for i in range(0,30):
        # 通过 获取验证码 按钮 的字样变化 来  判断 手机号 是否被注册过
        if  kuhua.isPhoneRegisted() :
            #手机号 已经被注册
            print pnum+' 已经被注册过了'
            logfile.write(pnum+' 已经被注册过了 \n')
            # 将 该手机号 拉入 黑名单
            mes.phoneBlacklist()
            # 释放掉 这个手机号
            mes.releasePhoneNumber()
            # 重新获取手机号
            pnum=mes.getPhoneNumber()
            # 重新 申请 获取验证码
            kuhua.requestVerfiyCode(pnum)
        else:
            # 如果 手机号 没有被注册过， 那么就向 验证码平台 获取 验证码
            vcode=mes.getVerifyCode()
            # 判断是否 获取到了 有效的验证码
            if vcode != '0000':
                # 如果获取到了 有效的验证码 就跳出循环 继续操作
                break
                # 如果没有 获取 有效的验证码 就 进入循环 重新获取手机号

    # 填写验证码
    kuhua.fillVerifycode(vcode)
    # 完成注册
    passw = kuhua.continueRegiste()
    # 将 注册过的手机号和 密码 写入到 文件中
    logfile.write('register '+pnum+'  '+passw+'\n')
    logfile.close()

    # 释放掉 手机号
    mes.releasePhoneNumber(pnum)





