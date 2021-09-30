# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:50:48 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        def zigzaglevelOrderBFS(root):
            """
            广度优先搜索方案
            BFS的本质，是维护一个队列，然后每层作为一个单元，入队和出队
            这里我用到了一个栈
            答案用到的是双端队列，差不太多。
            """

            queue = [root]
            stack = []
            level = 0
            # result = []
            while queue:
                # number = len(queue)
                result.append([])
                for _ in range(len(queue)):
                    # 本层出队/进栈
                    tempnode = queue.pop(0)
                    result[-1].append(tempnode.val)
                    stack.append(tempnode)

                while stack:
                    tempnode = stack.pop()
                    if level % 2:
                        if tempnode.left:
                            queue.append(tempnode.left)
                        if tempnode.right:
                            queue.append(tempnode.right)
                    else:
                        if tempnode.right:
                            queue.append(tempnode.right)
                        if tempnode.left:
                            queue.append(tempnode.left)
                
                level += 1
       
        
        if not root:
            return []
        result = []
        # depth = 0
        # levelOrderDFS(root,depth)
        zigzaglevelOrderBFS(root)
        
        return result

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    # input_List = ['RLRRLLRLRL','RL','RLRRRLLRLL','']
    input_List = TreeNode(1)
    input_List.left = TreeNode(2)
    input_List.right = TreeNode(3)
    input_List.left.left = TreeNode(4)
    input_List.right.right = TreeNode(5)
    # for i in input_List:

    result = solu.zigzagLevelOrder(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)