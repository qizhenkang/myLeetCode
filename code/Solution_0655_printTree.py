# -*- coding: utf-8 -*-
"""
Created on 2022/08/22 15:28:40

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


# Definition for a binary tree node.
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        """
        printTree _summary_

        感觉像是一个层序遍历解决的问题

        首先应该获取高度，然后再开

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            List[List[str]]: _description_
        """

        def get_root_depth(root: TreeNode, cur_height: int):
            if not root:
                return cur_height-1

            left_height = get_root_depth(root.left, cur_height+1)
            right_height = get_root_depth(root.right, cur_height+1)

            return max(left_height, right_height)

        height = get_root_depth(root, 0)

        row = height + 1
        col = 2**(height+1) - 1

        result: List[List[str]] = [["" for _ in range(col)] for _ in range(row)]

        def write_result(root: TreeNode, cur_height: int, position: Tuple[int, int]):
            if not root:
                return

            row = position[0]
            col = position[1]

            # print(row, col)
            result[row][col] = str(root.val)

            row_new = row+1

            dist = 2**(height-row-1)
            left_new = int(col - dist)
            right_new = int(col + dist)

            left_postion = (row_new, left_new)
            right_postion = (row_new, right_new)
            write_result(root.left, cur_height+1, left_postion)
            write_result(root.right, cur_height+1, right_postion)

            return
        write_result(root, 0, (0, int((col-1)/2)))

        return result


if __name__ == '__main__':

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    # node3 = TreeNode(3)
    # node4 = TreeNode(4)

    node1.left = node2
    # node1.right = node3
    # node2.right = node4

    solu = Solution()
    print(solu.printTree(node1))
