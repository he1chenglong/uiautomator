#-*-coding:utf8-*-
import sys
from uiautomator import device as d
# d.screen.on()
# #打开 QQ
# d(text="QQ").click()
# #点击联系人
# d.click(350,1230)

# devicesInfo=d.info
# print devicesInfo
#
# print devicesInfo[u'displayWidth']
# print devicesInfo['displayHeight']

ref={'x': 720, 'y': 1280}
# target={'x': devicesInfo[u'displayWidth'], 'y': devicesInfo['displayHeight']}

def convertx(nowx):
    newx=float(nowx)/ref['x']*target['x']
    print newx
    return newx

def converty(nowy):
    newy=float(nowy)/ref['y']*target['y']
    print newy
    return newy

def doclick(x,y):
    d.click(convertx(x),converty(y))

# doclick(350,1230)
    #file = sys.argv[1]
file='D:\python\monkeyrunner_py\qun_send.mr'
fp = open(file, 'r')

for line in fp:
        (cmd, rest) = line.split('|')
        try:
            # Parse the pydict
            rest = eval(rest)
            #print rest
            # print rest['x']
            # print rest['y']
            d.click(rest['x'],rest['y'])
        except:
            print 'unable to parse options'
            continue

def main():
    file = sys.argv[1]
    print file
    fp = open(file, 'r')


    # process_file(fp, device)
    fp.close();


if __name__ == '__main__':
    main()