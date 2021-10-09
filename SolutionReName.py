# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:58:46 2021

@author: qizhe
"""

import os, os.path, time

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
            # 遍历所有文件
            # if not os.path.isdir(name):
            #     if keyword in name :
            #         new_name = name.replace(keyword,'')
            #         os.renames(name,new_name)
            # else:
            #     rename(file + '\\' + name, keyword)
            #     os.chdir('...')
        # print('-----------------------分界线------------------------')
        # items = os.listdir(file)
        # for name in items:
        # print(name)
    
    def Name2MarkdownList(self,fileFolder):
        items = os.listdir(fileFolder)
        strlist = []
        pointer = 0
        for name in items:
            if name[:9] == 'Solution_':
                
                # 获取文件时间
                unixTime = os.path.getmtime(name)
                localTime = time.localtime(unixTime)
                timeStr = time.strftime('%Y/%m/%d',localTime)
                
                # print(name)
                strlist.append('')
                strlist[pointer] += '| '
                zeroFlag = 0
                numstr = ''
                for n in name[9:13]:
                    if n != '0':
                        zeroFlag = 1
                    if zeroFlag:
                        numstr += n
                strlist[pointer] += numstr
                strlist[pointer] += ' | '
                # title
                titleStr = ''
                for n in name[14:]:
                    if n =='.':
                        break
                    titleStr += n
                strlist[pointer] += titleStr
                strlist[pointer] += ' | '
                strlist[pointer] += ' | '
                strlist[pointer] += '[AC](./' + name +')'
                strlist[pointer] += ' | '
                strlist[pointer] += timeStr
                strlist[pointer] += ' | '
                strlist[pointer] += ' | '
                strlist[pointer] += ' | '
                
                # print(strlist[pointer])
                pointer +=1
        return strlist
                

if __name__ == '__main__':
    myfunc = myFunction()
    strlist = myfunc.Name2MarkdownList('.')
    for s in strlist:
        print(s)
    
    # myfunc.rename('E:\\Python_Projects\\LeetCode')
