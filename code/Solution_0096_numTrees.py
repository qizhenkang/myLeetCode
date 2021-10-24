# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 19:37:26 2021

@author: qizhe
"""


from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def numTrees(self, n: int) :
        """
        读题：
        1、和95题是一样的问题，但是一下就变了难度，感觉直接不是一个题型了
        2、应该是一个典型的动态规划的题目了吧？
        
        测试：
        1、10min，一次通过，性能良好
        
        答案：
        1、与答案的方法一，一模一样
        2、还可以直接数学求答案
        """
        dp = [0]*(n+1)
        
        dp[0] = 1
        dp[1] = 1
        # dp[2] = 2
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        
        return dp



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
    area = [1,2,80,100000,10000000]
    for s in range(1,6):
        result = solu.numTrees(s)
        output_Str = ' result = ' + str(result)
        print(output_Str)
        
    