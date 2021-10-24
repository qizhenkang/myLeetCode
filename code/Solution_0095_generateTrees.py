# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:01:36 2021

@author: qizhe
"""

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        读题：
        1、生成二叉搜索树，返回所有可能，应该是一个回溯
        2、没时间，等有时间再做，应该快了
        """
        
        def __dfs(n,result,current,headpre,used,total):
            print(n,total,current.val)
            if total == n:
                result.append(headpre.left)
                return
            for i in range(1,n):
                print(i)
                if used:
                    continue
                used[i] = True
                if i < current.val:
                    current.left = TreeNode(i)
                    __dfs(n,result,current.left,used,total+1)
                    current.left = None
                else:
                    current.right = TreeNode(i)
                    __dfs(n,result,current.right,used,total+1)
                    current.right = None
                used[i] = False
            
            return 
        
        
        result = []
        current = TreeNode()
        headpre = TreeNode(0, current)
        used = [False] * n
        __dfs(n,result,headpre.left,headpre,used,0)
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
    area = [1,2,80,100000,10000000]
    for s in range(8):
        result = solu.generateTrees(s)
    
        output_Str = ' result = ' + str(result)
        print(output_Str)
    