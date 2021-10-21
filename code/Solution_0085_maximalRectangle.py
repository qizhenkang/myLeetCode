# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:58:30 2021

@author: qizhe
"""
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        读题：
        1、感觉是一个典型的搜索问题，好像动态规划可以？
        2、为什么这么像单调栈？和前一个问题是不是有关系啊
        3、单调栈的思路为，dp记录每列高度，然后单调栈计算最大列
        
        测试：
        1、动态规划有问题，改为单调栈，感觉上是对的
        2、一次通过，性能一般
        
        答案：
        1、是答案中较好的一种
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [0]*n
        maxArea = 0
        stack = []
        for i in range(m):
            stack = []
            for j in range(n):
                if i == 0:
                    dp[j] = int(matrix[0][j])
                else:
                    dp[j] = 1 + dp[j] if int(matrix[i][j]) else 0
                # 这时候，开启单调栈的计算就完成了。
                while stack and dp[j] < dp[stack[-1]]:
                    curBar = stack.pop()
                    curHeight = dp[curBar]
                    curWidth = j - 1 - stack[-1] if stack else j
                    maxArea = max(maxArea,curHeight*curWidth)
                    # print(i,j,curBar,curHeight,curWidth,curHeight*curWidth,maxArea)
                stack.append(j)
            while stack:
                curBar = stack.pop()
                curHeight = dp[curBar]
                curWidth = n - 1 - stack[-1] if stack else n
                maxArea = max(maxArea,curHeight*curWidth)
                # print(i,j,curBar,curHeight,curWidth,curHeight*curWidth,maxArea)
                
                
            # print(dp)

        return maxArea
        
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
    # inputList = [2, 2]
    # time = 3
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.maximalRectangle(matrix)

    output_Str = ' result = ' + str(result)
    print(output_Str)