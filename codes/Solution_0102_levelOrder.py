# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:13:48 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode):
        """
        用递归的思路实现了深度优先遍历，完成了层次遍历
        这样容易写，但好像不是一个好方案。

        Parameters
        ----------
        root : TreeNode
            DESCRIPTION.

        Returns
        -------
        result : TYPE
            DESCRIPTION.

        """
        def levelOrderDFS(root,depth):
            """
            深度优先搜索方案
            """
            if not root:
                return
            
            if len(result) <= depth:
                result.append([root.val])
            else:
                result[depth].append(root.val)
            
            levelOrderDFS(root.left,depth+1)
            levelOrderDFS(root.right,depth+1)
        
        def levelOrderBFS(root):
            """
            广度优先搜索方案
            # BFS的本质，是维护一个队列，然后每层作为一个单元，入队和出队
            """

            queue = [root]
            # result = []
            while queue:
                # number = len(queue)
                result.append([])
                for _ in range(len(queue)):
                    # 本层出队
                    tempnode = queue.pop(0)
                    result[-1].append(tempnode.val)
                    if tempnode.left:
                        queue.append(tempnode.left)
                    if tempnode.right:
                        queue.append(tempnode.right)
                    
            
            
            return
        
        if not root:
            return []
        result = []
        # depth = 0
        # levelOrderDFS(root,depth)
        levelOrderBFS(root)
        
        return result

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    # input_List = ['RLRRLLRLRL','RL','RLRRRLLRLL','']
    input_List = TreeNode(3)
    # input_List.left = TreeNode(9)
    input_List.right = TreeNode(20)
    input_List.right.left = TreeNode(15)
    # input_List.right.right = TreeNode(7)
    # for i in input_List:

    result = solu.levelOrder(None)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)