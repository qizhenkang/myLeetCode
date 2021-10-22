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
import qizhenkangpylib
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
        dayslist = [0] * 365
        # 年份/月份统计 （当前共涉及2年）
        yearsDict = {}
        yearsDict[2020] = [0]*12
        yearsDict[2021] = [0] * 12
        
        
        for name in items:
            if name[:9] == 'Solution_':
                # 获取文件时间
                unixTime = os.path.getmtime(fileFolder+name)
                localTime = time.localtime(unixTime)
                # 统计小时分布
                # 直接tm_hour 这样统计出来的是0-60分，而画图却是以整点画图
                # 所以应该是+-30统计
                # hourslist[localTime.tm_hour] +=1
                if localTime.tm_min >= 30:
                    hourslist[(localTime.tm_hour + 1) %24] +=1
                else:
                    hourslist[localTime.tm_hour] +=1
                
                # 统计每日刷题数
                day_num = 364 - (int(time.mktime(time.localtime())) - int(time.mktime(localTime))) // (24 * 60 * 60)
                if day_num >= 364 or day_num <= 0:
                    # print(day_num)
                    pass
                else:
                    dayslist[day_num] += 1
                # 统计年月份刷题数
                yearsDict[localTime.tm_year][localTime.tm_mon-1] += 1

        return hourslist,yearsDict,dayslist
                

if __name__ == '__main__':
    myfunc = myFunction()
    # Statistics
    hourslist, yearsDict,dayslist = myfunc.statistics('./code/')
    # hourslist = [4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 22, 10, 5, 8, 10, 11, 7, 16, 1, 13, 16, 4, 2, 4]
    # yearsDict = {2020: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18], 2021: [0, 0, 0, 0, 0, 0, 0, 12, 68, 38, 0, 0]}
    # hourslist = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 20, 6, 6, 10, 12, 10, 19, 4, 10, 15, 11, 7, 9]
    # yearsDict = {2020: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18], 2021: [0, 0, 0, 0, 0, 0, 0, 12, 68, 70, 0, 0]}
    totalProblems = sum(hourslist)
     # 设置字号
    fontSize = 14
    fontSizeLabel = fontSize + 1
    fontSizeTitle = fontSize + 2
    myDPI = 150
    figSize = (8, 3.5)
    bottomSize = 0.15
    plt.style.use('dark_background')
    githubColor = [13/255,17/255,23/255] # 匹配github色彩
    fig_hours, ax = plt.subplots(figsize=figSize,facecolor=githubColor) # ,facecolor='black'
    hours = [str(i) for i in range(24)]
    hourslist_percent = [ i / totalProblems * 100  for i in hourslist]
    hourscmap = plt.cm.get_cmap('tab20c')
    hoursColor = hourscmap([ i/24 * 4 / 5 for i in range(24)])
    ax.bar(hours, hourslist_percent, width=0.5, label="Working Hours", color = hoursColor)
    ax.set_facecolor(githubColor)
    for label in ax.xaxis.get_ticklabels()[1::2]:
        label.set_visible(False)
    # ax.figure.set_size_inches(1, 1)
    
    # ax = sns.countplot(x="downNetwork", data=offline_data_shuffle)
    # plt.tight_layout()
   
    plt.xticks(size=fontSize)
    plt.yticks(size=fontSize)
    plt.xlabel('Time / hour',fontsize=fontSizeLabel)
    plt.ylabel('The percentage of problems / %',fontsize=fontSizeLabel)
    plt.title("Hourly Distribution of Zhenkang's Study Time", fontsize=fontSizeTitle) # 设置标题
    plt.subplots_adjust(bottom=bottomSize)
    plt.savefig('.//image//HourlyDistribution.jpg', dpi=myDPI,facecolor=githubColor)
    
    # plt.xticks(fontsize = 30)
    
    fig_months, ax = plt.subplots(figsize=figSize,facecolor=githubColor)
    months = [calendar.month_abbr[i] for i in range(1,13)]
    monthscmap = plt.cm.get_cmap('tab20c')
    totalProblems2021 = sum(yearsDict[2021])
    monthslist_percent = [i / totalProblems2021 * 100 for i in yearsDict[2021]]
    monthsColor = hourscmap([ i/12 * 4 / 5 for i in range(12)])
    ax.bar(months, monthslist_percent, width=0.5, label="Product_1", color=monthsColor)
    ax.set_facecolor(githubColor)
    fig_months.set_facecolor(githubColor)
    # plt.plot(hourslist)
    # print(hourslist)
    # print(yearsDict)
    
    # 设置字号
    # fontSize = 15
    plt.xticks(size=fontSize)
    plt.yticks(size=fontSize)
    plt.xlabel('Time / month',fontsize=fontSizeLabel)
    plt.ylabel('The percentage of problems / %',fontsize=fontSizeLabel)
    plt.title("Monthly Distribution of Zhenkang's Study Time in 2021", fontsize=fontSizeTitle) # 设置标题
    plt.subplots_adjust(bottom=bottomSize)
    plt.savefig('.//image//MonthlyDistribution.jpg', dpi=myDPI,facecolor=githubColor)
    # plt.xticks(fontsize = 30)
    
    fig_days, ax = plt.subplots(figsize = figSize,facecolor=githubColor)
    daysumlist = [0]
    for i in range(1,len(dayslist)):
        daysumlist.append(daysumlist[i-1]+dayslist[i])
    # print(daysumlist)
    ax.plot(daysumlist)
    ax.set_facecolor(githubColor)
    fig_months.set_facecolor(githubColor)
    
    plt.xticks(size=fontSize)
    plt.yticks(size=fontSize)
    plt.xlabel('Time / day',fontsize=fontSizeLabel)
    plt.ylabel('The number of problems',fontsize=fontSizeLabel)
    plt.title("The Cumulative Curve of Zhenkang's Daily Problems", fontsize=fontSizeTitle) # 设置标题
    plt.subplots_adjust(bottom=bottomSize)
    plt.savefig('.//image//DailyDistribution.jpg', dpi=myDPI,facecolor=githubColor)

    
    # Name2MarkdownList
    # strlist = myfunc.Name2MarkdownList('E:\\Python_Projects\\LeetCode\\')
    # for s in strlist:
    #     print(s)
    
    # Rename
    # myfunc.rename('E:\\Python_Projects\\LeetCode\\')
