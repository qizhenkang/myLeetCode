# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:18:55 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        """
        读题
        1、感觉就是一个中序遍历，因为这是一个二叉搜索树
        
        测试：
        1、一次通过，性能不错
        
        没时间看答案了，开始周赛了
        """
        
        def search(root,k,current):
            if not root:
                return
            if len(current) == 2:
                return
            search(root.left,k,current)
            current[0] += 1
            if current[0] == k:
                current.append(root.val)
                # print(root.val,current)
                return
            search(root.right,k,current)
            return
        current = [0]
        search(root,k,current)
        
        return current[1]

        

if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1
    # nums = [0,0,1,1,1,1,2,3,3]
    # # nums = [3,5,6,0,0,1,2]
    # # target = 2
    # nums = [1,0,1,1,1]
    # target = 0
    root1 = TreeNode(1)
    root2 = TreeNode(2,root1,None)
    root4 = TreeNode(4)
    root3 = TreeNode(3,root2,root4)
    root6 = TreeNode(6)
    root5 = TreeNode(5,root3,root6)
    k = 3
    

    result = solu.kthSmallest(root5,k)

    output_Str = ' result = ' + str(result)
    print(output_Str)