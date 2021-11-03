# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:47:33 2021

@author: Zhenkang
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:58:46 2021

@author: qizhe
"""
import re
import os, os.path, time
from pathlib import Path
# 字体设置

class MyListFunction:
    
    def getListStr(self):
        '''
        获取最新保存的文件，记录题号、题名
        '''
        dirpath = '.\\code\\'
        # ositems = os.listdir(dirpath)
        paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)
        # 获取最新的
        fileName = str(paths[-1])
        if fileName[:14] != 'code\Solution_':
            print('ERROR: ', fileName[:14])
            return ''
        # 显示当前名称
        print(fileName)
        
        # 分割字符串
        info = re.split(r'_|\.',fileName)
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
    
    result = myfunc.getListStr()
    
    print(result)
    
