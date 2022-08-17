# -*- coding: utf-8 -*-
"""
Created on 2022/08/17 17:29:55

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        deepestLeavesSum _summary_

        层序遍历，每层计算和

        10 min 解决问题 二次通过 错了一次理解题意错误 搞成最大了

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            int: _description_
        """

        stack: List[TreeNode] = [root]

        result = 0
        stack_level: List[TreeNode] = []
        cnt = 0
        while stack:

            node = stack.pop()
            if node.left:
                stack_level.append(node.left)

            if node.right:
                stack_level.append(node.right)

            cnt += node.val

            if not stack:
                result = cnt
                cnt = 0
                stack.extend(stack_level)
                stack_level: List[TreeNode] = []

        return result


# [50, null, 54, 98, 6, null, null, null, 34]

if __name__ == '__main__':
    solu = Solution()

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)
    root5 = TreeNode(5)

    root1.left = root2
    root1.right = root3
    root2.left = root4
    root2.right = root5
    print(solu.deepestLeavesSum(root1))

    root1 = TreeNode(50)
    root2 = TreeNode(54)
    root3 = TreeNode(98)
    root4 = TreeNode(6)
    root5 = TreeNode(34)

    root1 = root2
    root1.right = root2
    root2.left = root3
    root2.right = root4
    root4.right = root5
    print(solu.deepestLeavesSum(root1))
