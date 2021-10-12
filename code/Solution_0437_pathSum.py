# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:32:58 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        """
        深度优先遍历 + 前缀和 + 哈希表
        """
        
        prefix = {}
        prefix[0] = 1
        # 深度优先遍历
        def dfs(node,curr,targetSum):
            if not node:
                return 0
            
            # print(node.val,curr)
            # print(prefix)
            num = 0
            curr = curr + node.val
            # print(targetSum - curr)
            if curr - targetSum not in prefix.keys():
                prefix[curr - targetSum] = 0
            if curr not in prefix.keys():
                prefix[curr] = 0
                
            num += prefix[curr - targetSum]
            prefix[curr] += 1
            num += dfs(node.left,curr,targetSum)
            num += dfs(node.right,curr,targetSum)
            prefix[curr] -= 1
            
            return num

        return dfs(root,0 ,targetSum)
        
        


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('{[]{}()}')
    # input_list =
    input_List = [90]
    input_int = 200
    n1 = TreeNode(3)
    n2 = TreeNode(-2)
    n3 = TreeNode(3,n1,n2)

    n4 = TreeNode(1)
    n5 = TreeNode(2, n4)
    n6 = TreeNode(5, n5, n3)
    
    n7 = TreeNode(11)
    n8 = TreeNode(-3, n7)
    n9 = TreeNode(10, n8, n6)

    result = solu.pathSum(n9, 8)

    # while result:
    #     print(result.val)
    #     result = result.next
    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
