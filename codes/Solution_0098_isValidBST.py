# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:48:39 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        """
        从题目定义上，第一反应就是要递归调用
        
        第一反应用的是求左侧最值的方法，这样计算量比较大
        """
        # # 叶子节点，到底了，返回True
        # if not root.left and not root.right:
        #     return True
        
        # # 求左子树的最大值
        # leftMax = root.val - 1
        # tempNode = root.left
        # if tempNode:
        #     while tempNode.right:
        #         tempNode = tempNode.right
        
        #     leftMax = tempNode.val
        
        # # 求右子树的最小值
        # rightMin = root.val + 1
        # tempNode = root.right
        # if tempNode:
        #     while tempNode.left:
        #         tempNode = tempNode.left
            
        #     rightMin = tempNode.val
        
        # # 判断是否满足
        # if root.val <= leftMax or root.val >= rightMin:
        #     return False
        
        # # 递归调用，要求全部子节点满足
        # if not root.left:
        #     resultBool = self.isValidBST(root.right)
        # elif not root.right:
        #     resultBool = self.isValidBST(root.left)
        # else:
        #     resultBool = self.isValidBST(root.left) and self.isValidBST(root.right)
        
        """
        答案的意思用**中序遍历**，然后中序遍历是一个递增就可以了
        那么，容易想到的好方案，是迭代算法的中序遍历，然后逐个判断大小即可
        这个方案的时间和空间复杂度都很小
        """
        stack = []
        preVal = root.val
        firstFlag = 1
        # 中序遍历 典型迭代算法
        while stack or root:
            
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            # 遍历时，只需要判断，前后值顺序即可。
            if firstFlag:
                preVal = root.val
                firstFlag = 0
            elif root.val <= preVal:
                return False
            
            preVal = root.val
            root = root.right

        return True


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List = TreeNode(1)
    input_List.left = TreeNode(0)
    # input_List.right = TreeNode(3)
    
    result = solu.isValidBST(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)