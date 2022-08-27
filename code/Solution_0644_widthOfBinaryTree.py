# -*- coding: utf-8 -*-
"""
Created on 2022/08/27 14:51:03

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List, Optional, Tuple

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        widthOfBinaryTree _summary_

        感觉是一个层序遍历//先序遍历，搞一个队列，然后出队就是了，需要每次更新一下位置

        20min 一次通过，效率 73% 92% 还不错

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            int: _description_
        """

        result = 0
        queue: List[Tuple[TreeNode, int]] = [(root, 1)]

        while queue:
            first_flag = True
            queue_next: List[Tuple[TreeNode, int]] = []

            while queue:

                node, position = queue.pop(0)
                # print(node.val, position)
                next_position = 2*position
                if node.left:
                    queue_next.append((node.left, next_position-1))
                if node.right:
                    queue_next.append((node.right, next_position))
                if first_flag:
                    level_min = position
                    level_max = position
                    first_flag = False
                else:
                    level_max = max(level_max, position)

            level_width = level_max - level_min + 1
            result = max(result, level_width)
            queue = queue_next

        return result


if __name__ == '__main__':

    solu = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node3
    node1.right = node2
    node3.left = node5
    node3.right = node4
    node2.right = node6

    print(solu.widthOfBinaryTree(node1))

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node9 = TreeNode(9)

    node1.left = node3
    node3.left = node5
    node5.left = node6

    node1.right = node2
    node2.right = node9
    node9.left = node7

    print(solu.widthOfBinaryTree(node1))
