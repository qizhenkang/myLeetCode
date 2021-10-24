# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:20:28 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        第一反应还是中序遍历，然后判断顺序。
        
        二次读题：
        1、感觉像是一个二叉树的排序算法，要求不改变结构，就很像中序遍历+冒泡排序
        2、尝试一下递推栈，没那么简单，感觉不好下手
        3、思路上，就是二叉树的排序，需要中序遍历，需要交换位置
        4、只有两个节点被交换位置了，应该还简单一点
        """
        
        def __inorder(root):
            
            if root.left:
                __inorder(root.left)
            
            # print(root.val)
            # 先只交换值试试
            if root.right:
                __inorder(root.right)
            
            return 
        # __inorder(root)
        return
        # stack = [root]
        # while stack:
        #     for i in range(len(stack)):
        #         node = stack.pop()
        #         if node.right:
        #             stack.append(node.right)
        #         stack.append(node)
        #         if node.left:
        #             stack.append(node.left)
        #         else:
        #             stack.pop()
                
            # for i in range(len(stack)):
            #     print(stack[i].val)
        
        
        
        
        



if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List = TreeNode(1)
    input_List.left = TreeNode(2,TreeNode(4),TreeNode(5))
    input_List.right = TreeNode(3)
    
    result = solu.recoverTree(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)