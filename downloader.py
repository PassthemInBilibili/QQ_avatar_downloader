import requests
import time
import os
import random

if not(os.path.exists("Output")):
	os.mkdir(os.getcwd() + '\\Output')
#print(time.localtime(time.time()))
nowTime = time.localtime(time.time())
print("程序开启时间:", nowTime.tm_year, "年", nowTime.tm_mon, "月", nowTime.tm_mday, "日", nowTime.tm_hour, ":", nowTime.tm_min, ":", nowTime.tm_sec)
stry = str(nowTime.tm_year)
strmo = str(nowTime.tm_mon)
if len(strmo) == 1:
    strmo = "0" + strmo
strd = str(nowTime.tm_mday)
if len(strd) == 1:
    strd = "0" + strd
strh = str(nowTime.tm_hour)
if len(strh) == 1:
    strh = "0" + strh
strmi = str(nowTime.tm_min)
if len(strmi) == 1:
    strmi = "0" + strmi
strs = str(nowTime.tm_sec)
if len(strs) == 1:
    strs = "0" + strs
filename = stry + strmo + strd + "_" + strh + strmi + strs
mode = input("模式: ")
if mode == "a" or mode == "":
    nameMode = input("文件名格式：")

    # RANDOM: 随机
    # NAME: 昵称
    # ID: QQ号
    
    nameMode = nameMode if nameMode else "NAME"
    os.mkdir(os.getcwd() + '\\Output' + '\\' + filename)
    list = []
    try:
        with open("list.txt", "r") as lista:
            for each in lista.read().splitlines():
                list.append(each.split(" "))
    except:
        input("不存在list.txt，按下回车退出")
        exit()
    
    for a in list:
        try:
            int(a[0])
        except:
            numPlace = 1
        else:
            numPlace = 0
        if len(a) == 3:
            if a[2] == 'False':
                continue
        Download_addres= r"http://q1.qlogo.cn/g?b=qq&nk=" + a[numPlace] + r"&s=640"
        f=requests.get(Download_addres)
        with open('Output\\' + filename + '\\' + \
            nameMode.replace("NAME", a[1 if numPlace == 0 else 0]).replace("RANDOM", str(random.randint(10000000, 99999999))).replace("ID", a[numPlace])\
             + ".jpg","wb") \
        as code:
            code.write(f.content)
elif mode == "b":
    startnum = int(input("开始: "))
    endnum = int(input("结束: "))
    os.mkdir(os.getcwd() + '\\Output' + '\\' + filename)
    for each in range(startnum, endnum + 1):
        Download_addres= r"http://q1.qlogo.cn/g?b=qq&nk=" + str(each) + r"&s=640"
        f=requests.get(Download_addres)
        with open('Output\\' + filename + '\\' + str(each) + ".jpg","wb") as code:
            code.write(f.content)
elif mode == "c":
    geshi = input("内容: ").split(";")
    neednum = []
    for each in geshi:
        eachcheck = each.split("-")
        if len(eachcheck) == 1:
            neednum.append(int(eachcheck[0]))
        elif len(eachcheck) == 2:
            for eachnum in range(int(eachcheck[0]), int(eachcheck[1]) + 1):
                neednum.append(eachnum)
        elif len(eachcheck) == 3:
            for eachnum in range(int(eachcheck[0]), int(eachcheck[1]) + 1, int(eachcheck[2])):
                neednum.append(eachnum)
    os.mkdir(os.getcwd() + '\\Output' + '\\' + filename)
    for each in neednum:
        Download_addres= r"http://q1.qlogo.cn/g?b=qq&nk=" + str(each) + r"&s=640"
        f=requests.get(Download_addres)
        with open('Output\\' + filename + '\\' + str(each) + ".jpg","wb") as code:
            code.write(f.content)

