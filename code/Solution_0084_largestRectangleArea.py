# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:58:31 2021

@author: qizhe
"""
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        读题：
        1、感觉上有动态规划的意思，好像也有前缀和的意思
        2、核心思路是扫描，保存当前连续数字里 Max（最小数*长度）
        3、关键问题是，好像是不知道如何判断，从何处起始
        4、感觉是有状态的：连续 or 不连续
        5、这种感觉很像动态规划
        
        不会做了，10min了想不出来，看答案
        答案：
        1、单调栈，本质上是要找_每个矩形的左右边沿_然后取最大即可
        2、还没有完全理解
        """
        stack = [0]
        N = len(heights)
        areaList = [0]*N
        # left = 
        # for i in range(N):
        #     if stack:
        #         # 栈不为空 
                
        #     stack.append(heights[i])
        
    
        
        return 0
    
if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]
    n = 8
    inputList = [2,1,5,6,2,3]
    # time = 3
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","cot",'cog']
    # wordList = ["hot","dot","dog","lot","log","cog"]
    # beginWord = "a"
    # endWord = "c"
    # wordList = ["a","b","c"]
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.largestRectangleArea(inputList)

    output_Str = ' result = ' + str(result)
    print(output_Str)