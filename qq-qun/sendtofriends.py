#-*-coding:utf8-*-
import sys
import time
from uiautomator import device as d

#点击联系人
# d.click(350,1230)
# #点击 我的好友
# d(index='6').click()

for i in range(7,10):

    print str(i)
    #点击 第一个好友
    d(index=str(i),className='android.widget.FrameLayout').click()
    d(text=u'发消息').click()
    d(className='android.widget.EditText').clear_text()
    d(className='android.widget.EditText').set_text(u'你好')
    d(text=u'发送').click()
    d.press.back()
    time.sleep(2)
        #点击联系人
    d.click(350,1230)