# -*- coding: utf-8 -*-
"""
Created on 2022/08/09 14:04:04

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

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return self.__str__()


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        flatten _summary_

        -   二叉树的先序遍历
        -   移动指针

        二者同步进行或许有利于减小空间复杂度

        搞一个栈 入栈

        15 min 一次通过

        考后改进：
            -   所提方案不是最佳方案，用到了栈，本质上还是前序遍历 空间复杂度 O(n)
            -   最佳方案用了左右子树交换的技巧，可以做到空间复杂度 O(1)

        Warnings:
            Do not return anything, modify root in-place instead.

        Args:
            root (Optional[TreeNode]): _description_
        """
        if not root:
            return

        stack: List[TreeNode] = [root]

        head = TreeNode()
        head.right = root
        tail = head

        while stack:
            # print(stack)
            curp = stack.pop()

            tail.right = curp
            if curp.right:
                stack.append(curp.right)
            if curp.left:
                stack.append(curp.left)

            tail = curp
            tail.left = None

        # while head.right:
        #     head = head.right
        #     print(head.val)

        return


if __name__ == '__main__':
    node6 = TreeNode(6, None, None)
    node5 = TreeNode(5, None, node6)
    node4 = TreeNode(4, None, None)
    node3 = TreeNode(3, None, None)

    node2 = TreeNode(2, node3, node4)
    node1 = TreeNode(1, None, None)

    solu = Solution()
    result = solu.flatten(None)
    # assert result == True
