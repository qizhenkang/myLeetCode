# -*- coding: utf-8 -*-
"""
Created on 2022/08/30 10:16:00

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
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        insertIntoMaxTree _summary_

        今天没睡好，抄答案了

        他的意思是，给你的这个二叉树是一个特殊的二叉树
        是由一个数组生成的，构造的时候每次都选最大的。

        现在他在这个数组最后加入一个数，让你还是根据这个规则 更新二叉树

        那你需要做的其实是一直向右寻找，比较当前值和新值的大小，找到小的值，代替他
        然后将原来的作为他的左子树

        过程中，需要保存一下 parent 节点

        Args:
            root (Optional[TreeNode]): _description_
            val (int): _description_

        Returns:
            Optional[TreeNode]: _description_
        """

        parent, cur = None, root
        while cur:
            if val > cur.val:
                if not parent:
                    return TreeNode(val, root, None)
                node = TreeNode(val, cur, None)
                parent.right = node
                return root
            else:
                parent = cur
                cur = cur.right

        parent.right = TreeNode(val)
        return root
