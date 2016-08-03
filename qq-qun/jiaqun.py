#-*-coding:utf8-*-
import sys
import time
from uiautomator import device as d
import random
import linecache

def  randomline(yanfile='yanZheng.txt'):
    #获取行数
    count=len(open(yanfile,'rU').readlines())
    #生成随机数
    num=random.randrange(1,count,1)
    s=linecache.getline(yanfile,num)
    #编码转换 从UTF-8 转换成GBK
    return s.decode('gbk')

def  joinqun(qunhao):
    #填写群号
    d(className='android.widget.EditText').clear_text()
    d(className='android.widget.EditText').set_text(qunhao)
    # d(text=u'搜索').click()
    time.sleep(2)
    d(text=u'找群:').click()
    d(text=u'申请加群').click()
    time.sleep(2)
    #填写验证信息
    d(className='android.widget.EditText').clear_text()
    #d(className='android.widget.EditText').set_text(u"你好！ ")
    d(className='android.widget.EditText').set_text(randomline())
    time.sleep(2)
    d(text=u'发送').click()
    d(text=u'关闭').click()
    #等待20S再加下一个
    time.sleep(2)

def main():
    # num=['185406936','236477750','62637481']
    # for temp in num:
    #     jiaqun(temp)
    #从文件中读取要加的群号
    file='qunNumber.txt'
    fp = open(file, 'r')
    for line in fp:
        print 'join : '+line
        joinqun(line)

if __name__ == '__main__':
    main()