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
        
        没做出来，卡在了二叉树的深复制上
        
        答案：
        1、用递归，好像没发现有深复制的问题？
        2、答案的代码确实简洁，思路也清晰，就是不断的把问题变小，每步只考虑当前的做法
        """

        def generateTrees(start, end):
            if start > end:
                return [None,]
            
            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)
                
                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)
                # print(leftTrees)
                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            
            return allTrees
        
        return generateTrees(1, n) if n else []

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
    for s in range(3,4):
        result = solu.generateTrees(s)
        cnt = 1
        for re in result:
            temp = re
            print('left',end=' ')
            while temp:
                print(temp.val,end=' ')
                temp = temp.left
            temp = re
            print('right',end=' ')
            while temp:
                print(temp.val,end=' ')
                temp = temp.right
            print('--')
            print(cnt,' ---------')
            cnt +=1
        # output_Str = ' result = ' + str(result)
        # print(output_Str)
        
    