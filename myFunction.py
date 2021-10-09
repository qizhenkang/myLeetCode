# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:58:46 2021

@author: qizhe
"""

import os, os.path, time

import matplotlib.pyplot as plt
import matplotlib as mpl

class myFunction:

    def rename(self,file):
        ''' file: 文件路径    keyWord: 需要修改的文件中所包含的关键字 '''
        # start =time.clock()
        # os.chdir(file)
        items = os.listdir(file)
        print(os.getcwd())
        for name in items:
            # print(name)
            if name[:4] == 'Solu':
                if name == 'SolutionReName.py':
                    continue
                if name[-2:] == 'py' or name[-2:] == 'pp':
                    print(name)
                    new_name = name[:9] + '0' + name[9:]
                    print(new_name)

    
    def Name2MarkdownList(self,fileFolder):
        items = os.listdir(fileFolder)
        strlist = []
        pointer = 0
        for name in items:
            if name[:9] == 'Solution_':
                
                
                
                # print(name)
                strlist.append('')
                strlist[pointer] += '| '
                # Number
                zeroFlag = 0
                numstr = ''
                for n in name[9:13]:
                    if n != '0':
                        zeroFlag = 1
                    if zeroFlag:
                        numstr += n
                strlist[pointer] += numstr
                strlist[pointer] += ' | '
                # Title
                titleStr = ''
                for n in name[14:]:
                    if n =='.':
                        break
                    titleStr += n
                strlist[pointer] += titleStr
                strlist[pointer] += ' | '
                strlist[pointer] += ' | '
                # Status
                strlist[pointer] += '[AC](./' + name +')'
                strlist[pointer] += ' | '
                
                # Time
                # 获取文件时间
                unixTime = os.path.getmtime(name)
                localTime = time.localtime(unixTime)
                timeStr = time.strftime('%Y/%m/%d',localTime)
                strlist[pointer] += timeStr
                strlist[pointer] += ' | '
                strlist[pointer] += ' | '
                strlist[pointer] += ' | '
                
                # print(strlist[pointer])
                pointer +=1
        return strlist
    
    def statistics(self,fileFolder):
        """
        我想统计一下我的做题时间、做题曲线
        """
        items = os.listdir(fileFolder)
        # 每日提交时间统计
        hourslist = [0] * 24
        # 年份/月份统计 （当前共涉及2年）
        yearsDict = {}
        yearsDict[2020] = [0]*12
        yearsDict[2021] = [0] * 12

        for name in items:
            if name[:9] == 'Solution_':
                # 获取文件时间
                unixTime = os.path.getmtime(name)
                localTime = time.localtime(unixTime)
                hourslist[localTime.tm_hour] +=1
                yearsDict[localTime.tm_year][localTime.tm_mon-1] += 1

        return hourslist,yearsDict
                

if __name__ == '__main__':
    myfunc = myFunction()
    # Statistics
    hourslist, yearsDict = myfunc.statistics('.')
    
    fig_hours, ax = plt.subplots(figsize=(10, 7))
    hours = [str(i) for i in range(1,25)]
    ax.bar(hours, hourslist, width=0.5, label="Product_1", color="red")
    
    fig_months, ax = plt.subplots(figsize=(10, 7))
    months = [str(i) for i in range(1,13)]
    ax.bar(months, yearsDict[2021], width=0.5, label="Product_1", color="red")
    # plt.plot(hourslist)
    print(hourslist)
    print(yearsDict)
    
    
    # Name2MarkdownList
    # strlist = myfunc.Name2MarkdownList('.')
    # for s in strlist:
    #     print(s)
    
    # Rename
    # myfunc.rename('E:\\Python_Projects\\LeetCode')
