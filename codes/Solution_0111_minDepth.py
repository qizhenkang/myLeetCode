# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:23:50 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def minDepthBFS(root):
            """
            本质上就是一个广度优先遍历，当发现叶子节点后，直接return，从而达到最快的效果
            """
            if not root:
                return 0
            queue = [root]
            
            result = 0
            while queue:
                result += 1
                # number = len(queue)
                for _ in range(len(queue)):
                    # 本层出队
                    tempnode = queue.pop(0)
                    
                    if not tempnode.left and not tempnode.right:
                        return result
                    if tempnode.left:
                        queue.append(tempnode.left)
                    if tempnode.right:
                        queue.append(tempnode.right)

            return result

        return minDepthBFS(root)

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    # input_List = ['RLRRLLRLRL','RL','RLRRRLLRLL','']
    input_List = TreeNode(3)
    input_List.left = TreeNode(9)
    input_List.right = TreeNode(20)
    input_List.right.left = TreeNode(15)
    input_List.right.right = TreeNode(7)
    # for i in input_List:

    result = solu.minDepth(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)