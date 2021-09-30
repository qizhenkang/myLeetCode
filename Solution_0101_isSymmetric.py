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
    def isSymmetric(self, root: TreeNode) -> bool:
        # 迭代好像简单一点
        
        lc_stack = []
        rc_stack = []
        lc = root.left
        rc = root.right
        
        # 本质上，是对左右子树的遍历
        # 对左子树采用左中右遍历
        # 对右子树采用右中左遍历
        while lc_stack or rc_stack or lc or rc:
            while lc and rc:
                lc_stack.append(lc)
                rc_stack.append(rc)
                # if lc.val != rc.val:
                #     return False
                lc = lc.left
                rc = rc.right
            if lc or rc:
                return False
            
            lc = lc_stack.pop()
            rc = rc_stack.pop()
            
            if lc.val != rc.val:
                return False
                
            lc = lc.right
            rc = rc.left

        return True

        


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List = TreeNode(2)
    input_List.left = TreeNode(3)
    input_List.right = TreeNode(3)
    input_List.left.left = TreeNode(4)
    input_List.left.right = TreeNode(5)
    input_List.right.left = TreeNode(5)
    # input_List.right.right = TreeNode(3)

    result = solu.isSymmetric(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)