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
        """

        stack = []
        heights = [0] + heights + [0]
        N = len(heights)
        result = 0
        for i in range(1, N):
            while stack and (i == N or heights[i] < heights[stack[-1]]):
                curHeight = heights[stack.pop()]
                # print(i,stack)
                if stack:
                    curWidth = i - 1 - stack[-1]
                else:
                    curWidth = i - 1

                # print(curHeight, '*', '(', i, '-', stack[-1], ') = ', curHeight * curWidth)
                # print(i, curHeight, '*', curWidth, ' = ', curHeight * curWidth)

                result = max(result, curHeight * curWidth)
            # 栈应当存左边界
            # if i < N:
            stack.append(i)
        return result


if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]

    n = 8
    inputList = [1]
    inputList = [2, 1, 5, 6, 2, 3]
    inputList = [2, 2]
    # time = 3
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.largestRectangleArea(inputList)

    output_Str = ' result = ' + str(result)
    print(output_Str)