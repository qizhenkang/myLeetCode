# -*- coding: utf-8 -*-
"""
Created on 2022/09/02 16:30:29

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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        longestUnivaluePath _summary_

        二叉树的搜索问题，深度优先搜索就很合适

        如果与父节点一致，则 +1 

        如果与父节点不一致，则清零 刚好

        12 min 提交一次 出错了 理解题意有误 打乱思路了

        没想明白 抄答案了 他的意思本质上是，最大路径，一定是在根节点找到的
        所以 他只考虑根节点与子节点相同的情况才保存一下

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            int: _description_
        """

        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left1 = left + 1 if node.left and node.left.val == node.val else 0
            right1 = right + 1 if node.right and node.right.val == node.val else 0
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)
        dfs(root)
        return ans


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(4)
    node5 = TreeNode(4)
    node6 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node5.right = node6

    solu = Solution()

    print(solu.longestUnivaluePath(node1))  # 2
