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

        测试：
        1、错了3次，理解不到位，还需要在看
        2、又过了一天，再调试，懂了，其实是目标搞清楚了，就是要把握本质
        3、本质就是要对比每一个小矩形的最大面积，逐步向前扫描，若单调增（or不减），则压栈
        4、若减，则出栈，表明至少找到了一个
        """

        stack = []
        # heights = heights
        N = len(heights)
        result = 0
        for i in range(N+1):
            while stack and (i == N or heights[i] < heights[stack[-1]]):# (i == N or heights[i] < heights[stack[-1]]):
                # 当前Bar的最大面积
                curBar = stack.pop()
                # 当前高度
                curHeight = heights[curBar]
                # 当前右端为i-1，当前左端为栈
                curLeft = stack[-1] if stack else -1
                curWidth = i - 1 - curLeft
                
                # print(curHeight, '*', '(', i, '-', stack[-1], ') = ', curHeight * curWidth)
                # print(i, curHeight, '*', curWidth, ' = ', curHeight * curWidth)

                result = max(result, curHeight * curWidth)
                print(i,stack,curLeft,curBar,curHeight * curWidth)
            if i < N:
                stack.append(i)
        # while stack:
            
        # print(stack)
        return result


if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]

    n = 8
    inputList = [1]
    inputList = [2, 0, 5, 6, 2, 3]
    # inputList = [2, 2]
    # time = 3
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.largestRectangleArea(inputList)

    output_Str = ' result = ' + str(result)
    print(output_Str)