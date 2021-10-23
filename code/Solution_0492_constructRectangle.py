# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:12:33 2021

@author: qizhe
"""
from typing import List
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        读题：
        1、感觉是一个二分搜索的问题
        2、上界为 int(sqrt(area))
        3、感觉好像不好找
        
        测试：
        1、LW反了错了一次，改正后一次通过，用时10min
        
        答案：
        1、答案也只有暴力法，这题没什么他意思
        """
        right = int(math.sqrt(area))
        result = [area,1]
        for i in range(right,1,-1):
            if area % i == 0:
                result = [int(area)//i,i]
                break
        # while mid:
        #     pass
        return result
        
if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]

    n = 8
    inputList = [1]
    inputList = [2, 0, 5, 6, 2, 3]
    matrix = [["0","1","0","1","0"],["1","1","0","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = []
    matrix = [["0"],['1']]
    matrix = [["1","0"]]
    ss = ['12',"23",'20310','06','011106','111111111111111111111111111111111111111111111']
    ss = ['1234','2101','123123']
    area = [0,1,2,80,100000,10000000]
    for s in area:
        result = solu.constructRectangle(s)
    
        output_Str = ' result = ' + str(result)
        print(output_Str)
    