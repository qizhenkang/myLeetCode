# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:01:57 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        """
        中序遍历 递归算法

        """
        # 中序遍历
        # 读左子树，返回左子树列表
        # 读根节点，加入列表
        # 读右子树，返回右子树列表
        
        # 若子树为空，则返回空列表
        
        # if root is None:
        #     return []
        # result = []
        
        # result = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        """
        中序遍历 迭代算法
        """
        if not root:
            return []
        result = []
        NodeStack = []
        while NodeStack or root:
            # print(NodeStack) 
            while root:
                NodeStack.append(root)
                root = root.left
            root = NodeStack.pop()
            result.append(root.val)
            root = root.right
        
        return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List = TreeNode(1)
    input_List.left = TreeNode(2)
    input_List.right = TreeNode(3)
    
    result = solu.inorderTraversal(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)