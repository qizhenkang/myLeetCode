# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 23:39:31 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        """
        不是很懂，看了答案，意思是：
        1、先序遍历第一个就是根节点，然后是左子树，然后是右子树
        2、中序遍历先左子树，然后是根节点，然后是右子树
        3、根据根节点位置，可以判断左右子树，从而完成递归
        """
        def mybuildTree(preorderStart,preorderEnd, inorderStart, inorderEnd):
            """
            参考答案，用位置代替列表传递
            充分发挥哈希表的作用
            """
            # 进行遍历
            if preorderStart>=preorderEnd or inorderStart>=inorderEnd:
                # print(preorderStart,preorderEnd, inorderStart, inorderEnd)
                return None
            rootVal = preorder[preorderStart]
            # 对于这个的理解是关键，其本质上是计算左子树的宽度
            aimposi = inorderDict[rootVal] - inorderStart
            
            # print(preorderStart,preorderEnd, inorderStart, inorderEnd,aimposi,rootVal)
            headNode = TreeNode(rootVal)
            headNode.left = mybuildTree(preorderStart + 1,preorderStart + 1 + aimposi,inorderStart,inorderStart+aimposi)
            headNode.right = mybuildTree(preorderStart + aimposi+1,preorderEnd, inorderStart+aimposi+1,inorderEnd)
            
            return headNode
        
        N = len(inorder)
        inorderDict = {h:i for i,h in enumerate(inorder)}
        return mybuildTree(0,N,0,N)


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
    
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    result = solu.buildTree(preorder, inorder)

    while result:
        print(result.val)
        result = result.right

    # output_Str = 'result = ' + str(result)
    # print(output_Str)
