# -*- coding: utf-8 -*-
"""
Created on 2022/08/19 19:46:46

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        sumNumbers 

        是一个二叉树遍历，叶子结点的时候加一下就可以了

        8 min 一次通过 和答案一模一样

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            int: _description_
        """

        def dfs(root: TreeNode, temp_num: int) -> int:

            if not root:
                return 0

            if not root.left and not root.right:
                return temp_num*10 + root.val

            a = dfs(root.left, temp_num*10+root.val)
            b = dfs(root.right, temp_num*10+root.val)

            return a+b

        return dfs(root, 0)


if __name__ == '__main__':

    solu = Solution()

    root = TreeNode(4)
    node1 = TreeNode(9)
    node2 = TreeNode(0)
    node3 = TreeNode(5)
    node4 = TreeNode(1)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    print(solu.sumNumbers(root))

    print(solu.sumNumbers(TreeNode(4, TreeNode(3), TreeNode(1))))
