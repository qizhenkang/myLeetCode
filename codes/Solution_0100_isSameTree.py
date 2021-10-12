# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:55:56 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        一遍过，其实就是一个遍历就好了
        用了递归的方法
        我好像一遍就写出了正确答案 哈哈
        2021/09/04
        
        """

        if not p and not q:
            # 全为None，则为叶子节点
            return True
        elif not p or not q:
            # 有一个为None，必然为False
            return False
        else:
            # 二者都存在
            if p.val != q.val:
                return False
            
            resultDecision = self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        return resultDecision
        


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List = TreeNode(1)
    input_List.left = TreeNode(2)
    input_List.right = TreeNode(3)
    
    input_List2 = TreeNode(1)
    input_List2.left = TreeNode(2)
    input_List2.right = TreeNode(4)
    
    result = solu.isSameTree(input_List,input_List2)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)