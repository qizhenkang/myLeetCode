# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:07:14 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # 来个递归吧，简单
        
        if not root:
            return 0
        
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

        


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List = TreeNode(2)
    input_List.left = TreeNode(3)
    input_List.right = TreeNode(3)
    # input_List.left.left = TreeNode(4)
    # input_List.left.right = TreeNode(5)
    # input_List.right.left = TreeNode(5)
    # input_List.right.right = TreeNode(3)

    result = solu.maxDepth(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)