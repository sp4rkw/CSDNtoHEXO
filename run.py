
# -*- coding: UTF-8 -*-
'''
Desprition:
    此脚本用来将csdn博客中的图片下载并且进行对应替换../../../../image/xxx.jpg

Author:
    Sp4rkW   http://www.anquanxiaozhan.com

Modify:2019-07-13 12:50:28
'''
import re,os,requests



'''
Desprition:
    这个函数用来遍历指定目录下面的md文件，并将所有md文件的绝对路径写入数组

Parameters:
    mdpath  传入md文件夹的绝对路径

Returns:
    DirList2 传出每一个md文件的绝对路径

Modify:2019-07-13 13:07:03
'''
def FindPath(mdpath):
    DirList1 =  os.listdir(mdpath)
    DirList2 = [mdpath+x for x in DirList1]
    return DirList2

'''
Desprition:
    这个函数用来下载md文件中的csdn图片并对其进行重命名，之后将对应位置进行替换

Parameters:
    mdfile        md文件的路径
    pcfile       图片文件存放路径
    picturenum   图片编号

Returns:
    picturenum   图片编号

Modify:2019-07-20 15:32:00
'''

def ImgReplace(mdfile,pcfile,picturenum):
    lines = []
    with open(mdfile,encoding="UTF-8") as f:
        lines = f.readlines()
        num = len(lines)
    for i in range(num):
        MatchObj = re.search(r'\!\[.*\](.*img-blog.csdn.net.*)',lines[i])
        if MatchObj:
            MatchData = MatchObj.group()
            MatchData = MatchData.replace('!','')
            MatchData = MatchData.replace('[','')
            MatchData = MatchData.replace(']','')
            MatchData = MatchData.replace('(','')
            MatchData = MatchData.replace(')','')
            MatchData = MatchData.replace('这里写图片描述','')         # 这里可以自行用replace增加更多规则
            MatchData = MatchData.replace('简易计算器','')
            MatchData = MatchData.replace('eval测试','')
            MatchData = MatchData.replace('演示','')
            MatchData = MatchData.replace('在这里插入图片描述','')
            if('https' not in MatchData):
                MatchData = 'https:'+MatchData
            html = requests.get(MatchData)
            ImagePath = pcfile+str(picturenum)+".png"
            reldata ="![](../../../../image/"+str(picturenum)+".png)"  #这里为服务器上图片路径，自行修改
            lines[i] = re.sub(r'\!\[.*\](.*img-blog.csdn.net.*)',reldata,lines[i])
            picturenum = picturenum + 1
            with open(ImagePath,"wb")as f:
                f.write(html.content)
    open(mdfile,'w',encoding="UTF-8").writelines(lines)
    for i in range(num):
        MatchObj = re.search(r'\!\[.*\](.*img-blog.csdnimg.cn.*)',lines[i])
        if MatchObj:
            MatchData = MatchObj.group()
            MatchData = MatchData.replace('!','')
            MatchData = MatchData.replace('[','')
            MatchData = MatchData.replace(']','')
            MatchData = MatchData.replace('(','')
            MatchData = MatchData.replace(')','')
            MatchData = MatchData.replace('这里写图片描述','')
            MatchData = MatchData.replace('在这里插入图片描述','')
            if('https' not in MatchData):
                MatchData = 'https:'+MatchData
            html = requests.get(MatchData)
            ImagePath = pcfile+str(picturenum)+".png"
            reldata ="![](../../../../image/"+str(picturenum)+".png)"   #这里为服务器上图片路径，自行修改
            lines[i] = re.sub(r'\!\[.*\](.*img-blog.csdnimg.cn.*)',reldata,lines[i])
            picturenum = picturenum + 1
            with open(ImagePath,"wb")as f:
                f.write(html.content)
    open(mdfile,'w',encoding="UTF-8").writelines(lines)
    return picturenum


def ImgReplaceTest(mdfile,pcfile,picturenum):
    lines = []
    with open(mdfile,encoding="UTF-8") as f:
        lines = f.readlines()
        num = len(lines)
    for i in range(num):
        MatchObj = re.search(r'\!\[.*\](.*img-blog.csdn.net.*)',lines[i])
        if MatchObj:
            MatchData = MatchObj.group()
            MatchData = MatchData.replace('!','')
            MatchData = MatchData.replace('[','')
            MatchData = MatchData.replace(']','')
            MatchData = MatchData.replace('(','')
            MatchData = MatchData.replace(')','')
            MatchData = MatchData.replace('这里写图片描述','')         # 这里可以自行用replace增加更多规则
            MatchData = MatchData.replace('简易计算器','')
            MatchData = MatchData.replace('eval测试','')
            MatchData = MatchData.replace('演示','')
            MatchData = MatchData.replace('在这里插入图片描述','')
            if('https' not in MatchData):
                MatchData = 'https:'+MatchData
        print(MatchData)
    for i in range(num):
        MatchObj = re.search(r'\!\[.*\](.*img-blog.csdnimg.cn.*)',lines[i])
        if MatchObj:
            MatchData = MatchObj.group()
            MatchData = MatchData.replace('!','')
            MatchData = MatchData.replace('[','')
            MatchData = MatchData.replace(']','')
            MatchData = MatchData.replace('(','')
            MatchData = MatchData.replace(')','')
            MatchData = MatchData.replace('这里写图片描述','')
            MatchData = MatchData.replace('在这里插入图片描述','')
            if('https' not in MatchData):
                MatchData = 'https:'+MatchData
        print(MatchData)
    return picturenum




if __name__ == "__main__":
    FilePath = input("请输入md文件夹绝对路径:")
    PcPath = input("请输入图片文件夹绝对路径:")
    DirList = FindPath(FilePath)
    now = 1
    for line in DirList:
        now =  ImgReplace(line,PcPath,now)
        print(line+"   已经完成替换")
        print('当前图片数量为:   '+str(now))