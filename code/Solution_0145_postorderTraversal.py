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
    def postorderTraversal(self, root):
        """
        后序遍历 递归算法

        """
        # 中序遍历
        # 读左子树，返回左子树列表
        # 读根节点，加入列表
        # 读右子树，返回右子树列表
        
        # 若子树为空，则返回空列表
        
        # if root is None:
        #     return []
        # result = []
        
        # result = self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] 
        """
        后序遍历 迭代算法
        """
        if not root:
            return []
        result = []
        NodeStack = []
        prev = None
        while NodeStack or root:
            # for i in NodeStack:
            #     print(len(NodeStack),i.val) 
            # print(result)
            while root:
                NodeStack.append(root)
                # result.append(root.val)
                root = root.left
            root = NodeStack.pop()
            if not root.right or root.right == prev:    
                # 没有左/右孩子，则将该节点加入结果
                result.append(root.val)
                prev = root
                root = None
            else:
                # 如果有右孩子，则
                # NodeStack.append(root.right)
                NodeStack.append(root)
                root = root.right
        return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List = TreeNode(1)
    input_List.left = TreeNode(2)
    input_List.right = TreeNode(3)
    
    result = solu.postorderTraversal(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)