# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:33:48 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        """
        只是从上一个题的前序变成了后序
        """
        def mybuildTree(inorderStart, inorderEnd, postorderStart, postorderEnd):
            
            if inorderStart >= inorderEnd:
                return None
            
            rootval = postorder[postorderEnd-1]
            # 对于这个的理解是关键，其本质上是计算右子树的宽度
            aimposi = inorderEnd - 1 - inorderDict[rootval] 
            # print(inorderStart, inorderEnd, postorderStart, postorderEnd,aimposi,rootval)
            
            headNode = TreeNode(rootval)
            headNode.left = mybuildTree(inorderStart, inorderEnd - aimposi - 1, postorderStart, postorderEnd - aimposi -1)
            headNode.right = mybuildTree(inorderEnd - aimposi, inorderEnd, postorderEnd - aimposi - 1, postorderEnd-1)

            return headNode
        N = len(inorder)
        inorderDict = {n:i for i,n in enumerate(inorder)}
        return mybuildTree(0, N, 0, N)
        
        
    
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('{[]{}()}')
    # input_list =
    input_List = [90]
    input_int = 200
    n1 = TreeNode(15)
    n2 = TreeNode(7)
    n3 = TreeNode(20,n1,n2)

    n4 = TreeNode(9)
    # n5 = TreeNode(2, n4)
    # n6 = TreeNode(5, n5, n3)
    
    # n7 = TreeNode(11)
    # n8 = TreeNode(-3, n7)
    n9 = TreeNode(3, n3, n4)
    
    postorder = [9,15,7,20,3]
    inorder = [9,3,15,20,7]

    result = solu.buildTree(inorder,postorder)

    while result:
        print(result.val)
        result = result.right

    # output_Str = 'result = ' + str(result)
    # print(output_Str)
