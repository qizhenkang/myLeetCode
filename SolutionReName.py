# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:58:46 2021

@author: qizhe
"""

import os ,os.path

def rename(file):
    ''' file: 文件路径    keyWord: 需要修改的文件中所包含的关键字 '''
    # start =time.clock()
    # os.chdir(file)
    items = os.listdir(file)
    print(os.getcwd())
    for name in items:
        # print(name)
        if name[:4] =='Solu':
            if name[-2:] == 'py' or name[-2:] == 'pp' :
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
 
rename('E:\\Python_Projects\\LeetCode')