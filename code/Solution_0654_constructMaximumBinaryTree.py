# -*- coding: utf-8 -*-
"""
Created on 2022/08/20 10:03:25

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        constructMaximumBinaryTree _summary_

        读题明白了，先找最大值，然后划分左右二叉树

        递归调用 5 min  一次通过 

        这属于这道题的简单解法 时间复杂度较大

        实际答案为单调栈 没仔细懂

        Args:
            nums (List[int]): _description_

        Returns:
            Optional[TreeNode]: _description_
        """

        if not nums:
            return None

        # find the max point
        num_max = max(nums)
        num_index = 0
        for i in range(len(nums)):
            if nums[i] == num_max:
                num_index = i
                break

        node = TreeNode(num_max)
        node.left = self.constructMaximumBinaryTree(nums[:num_index])
        node.right = self.constructMaximumBinaryTree(nums[num_index+1:])

        return node


if __name__ == '__main__':
    pass
