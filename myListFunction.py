# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:47:33 2021

@author: Zhenkang
"""

import re
import os, os.path, time
from pathlib import Path
# 字体设置

class MyListFunction:
    
    def getNewfileName(self):
        '''
        获取最新保存的文件，记录题号、题名
        '''
        dirpath = '.\\code\\'
        # ositems = os.listdir(dirpath)
        paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)
        # print(paths)
        # 获取最新的
        fileName = str(paths[-1])
        if fileName[:14] != 'code\Solution_':
            print('ERROR: ', fileName)
            return ''
        # 显示当前名称
        # print(fileName)
        fileName = fileName[5:]
        return fileName
        
        
        
    
    def getListStr(self,fileName):
        # 分割字符串
        info = re.split(r'_|\.',fileName)
        # print(info)
        # 获取信息
        number,name =  str(int(info[1])),info[2]
        
        dateTime = time.localtime()
        mday = str(dateTime.tm_mday) if dateTime.tm_mday >= 10 else  '0'+str(dateTime.tm_mday)
        date = str(dateTime.tm_year) + '/' +  str(dateTime.tm_mon) + '/' + mday
        
        # 生成字符串
        resultStr = ' | '
        resultStr += number + ' | ' 
        resultStr += name+ ' | ' 
        resultStr += '--- | ' 
        resultStr += '[--](./code/Solution_' + info[1] +'_' + info[2] + '.py)' + ' | ' 
        resultStr += date + ' | ' 
        resultStr += '--- | ' 
        resultStr += '--- | ' 
        
        return resultStr
                

if __name__ == '__main__':
    myfunc = MyListFunction()
    
    fileName = myfunc.getNewfileName()
    

    # a = 'Solution_2057_smallestEqual.py'
    # b = 'Solution_2058_nodesBetweenCriticalPoints.py'
    # c = 'Solution_2059_minimumOperations.py'
    # d = 'Solution_2060_possiblyEquals.py'
    # myName = [a,b,c,d]
    # for i in myName:
    #     print(myfunc.getListStr(i))
    
    result = myfunc.getListStr(fileName)
    
    print(result)
    
