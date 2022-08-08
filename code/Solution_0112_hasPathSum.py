# -*- coding: utf-8 -*-
"""
Created on 2022/08/08 19:41:18

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        hasPathSum _summary_

        明显是一个深度优先搜索的问题

            -   搜索是显然的
            -   深度优先是因为他找到 1 个满足就可以

        通过用时: 13 min

        和答案几乎一致

        Args:
            root (Optional[TreeNode]): _description_
            targetSum (int): _description_

        Returns:
            bool: _description_
        """
        result = False

        def search_node(root: TreeNode, count: int) -> bool:

            if not root:
                return False
            # print(root.val, count)
            if not root.left and not root.right:
                # 叶子结点
                if count + root.val == targetSum:
                    return True
                else:
                    return False
            result_left = False
            result_right = False
            result_left = search_node(root.left, count + root.val)
            result_right = search_node(root.right, count + root.val)

            return result_left or result_right

        result = search_node(root, 0)

        return result


if __name__ == '__main__':
    node1 = TreeNode(7, None, None)
    node2 = TreeNode(2, None, None)
    node3 = TreeNode(11, node1, node2)
    node4 = TreeNode(4, node3, None)
    node5 = TreeNode(8, None, None)
    node6 = TreeNode(5, node4, node5)

    solu = Solution()
    result = solu.hasPathSum(node6, 22)
    assert result == True

    node1 = TreeNode(3, None, None)
    node2 = TreeNode(2, None, None)
    node3 = TreeNode(1, node1, node2)

    solu = Solution()
    result = solu.hasPathSum(node3, 5)
    assert result == False
