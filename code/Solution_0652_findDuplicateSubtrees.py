# -*- coding: utf-8 -*-
"""
Created on 2022/09/05 11:09:02

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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        findDuplicateSubtrees _summary_

        抄答案了，太麻烦了。

        找相同子树。

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            List[Optional[TreeNode]]: _description_
        """

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            tri = (node.val, dfs(node.left), dfs(node.right))
            if tri in seen:
                (tree, index) = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx

        idx = 0
        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)
