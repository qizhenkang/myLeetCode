# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:58:46 2021

@author: qizhe
"""

import os, os.path, time
import calendar
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
# 字体设置
rcParams['font.family'] = 'Times New Roman'

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
                unixTime = os.path.getmtime(fileFolder+name)
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
    totalProblems = sum(hourslist)
    
    plt.style.use('dark_background')
    githubColor = [13/255,17/255,23/255] # 匹配github色彩
    fig_hours, ax = plt.subplots(figsize=(8, 4),facecolor=githubColor) # ,facecolor='black'
    hours = [str(i) for i in range(24)]
    hourslist_percent = [ i / totalProblems * 100  for i in hourslist]
    hourscmap = plt.cm.get_cmap('tab20c')
    hoursColor = hourscmap([ i/24 * 4 / 5 for i in range(24)])
    ax.bar(hours, hourslist_percent, width=0.5, label="Working Hours", color = hoursColor)
    ax.set_facecolor(githubColor)
    for label in ax.xaxis.get_ticklabels()[1::2]:
        label.set_visible(False)
    
    
    # 设置字号
    fontSize = 10
    myDPI = 150
    plt.xticks(size=fontSize)
    plt.yticks(size=fontSize)
    plt.xlabel('Time / hour',fontsize=fontSize+3)
    plt.ylabel('The percentage of problems / %',fontsize=fontSize+3)
    plt.title("Hourly Distribution of Zhenkang's Study Time", fontsize=fontSize+5) # 设置标题
    plt.savefig('.//image//HourlyDistribution.jpg', dpi=myDPI,facecolor=githubColor)
    
    # plt.xticks(fontsize = 30)
    
    fig_months, ax = plt.subplots(figsize=(8, 4),facecolor=githubColor)
    months = [calendar.month_abbr[i] for i in range(1,13)]
    monthscmap = plt.cm.get_cmap('tab20c')
    totalProblems2021 = sum(yearsDict[2021])
    monthslist_percent = [i / totalProblems2021 * 100 for i in yearsDict[2021]]
    monthsColor = hourscmap([ i/12 * 4 / 5 for i in range(12)])
    ax.bar(months, monthslist_percent, width=0.5, label="Product_1", color=monthsColor)
    ax.set_facecolor(githubColor)
    fig_months.set_facecolor(githubColor)
    # plt.plot(hourslist)
    print(hourslist)
    print(yearsDict)
    
    # 设置字号
    # fontSize = 15
    plt.xticks(size=fontSize)
    plt.yticks(size=fontSize)
    plt.xlabel('Time / month',fontsize=fontSize+3)
    plt.ylabel('The percentage of problems / %',fontsize=fontSize+3)
    plt.title("Monthly Distribution of Zhenkang's Study Time", fontsize=fontSize+5) # 设置标题
    plt.savefig('.//image//MonthlyDistribution.jpg', dpi=myDPI,facecolor=githubColor)
    # plt.xticks(fontsize = 30)
    
    
    # Name2MarkdownList
    # strlist = myfunc.Name2MarkdownList('E:\\Python_Projects\\LeetCode\\')
    # for s in strlist:
    #     print(s)
    
    # Rename
    # myfunc.rename('E:\\Python_Projects\\LeetCode\\')
