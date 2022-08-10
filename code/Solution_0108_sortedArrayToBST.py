# -*- coding: utf-8 -*-
"""
Created on 2022/08/09 20:46:33

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

    def levelOrder(self) -> List[List['TreeNode']]:
        """
        levelOrder _summary_

        二叉树的层序遍历 
            含 None

        Returns:
            _type_: _description_
        """

        result: List[List[TreeNode]] = []
        queue: List[TreeNode] = [self]

        while any(queue):

            level: List[int] = []
            for _ in range(len(queue)):
                # 本层出队
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level.append(None)
                    queue.append(None)
                    queue.append(None)
            result.append(level)

        return result


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        sortedArrayToBST _summary_

        中序遍历为顺序，即为所谓的二叉搜索树

        nums 本身就是升序排列的了，所以不需要排序，就是生成一个 bst

        想了 5 min 不会


        Args:
            nums (List[int]): _description_

        Returns:
            Optional[TreeNode]: _description_
        """

        def helper(left, right) -> TreeNode:

            if left >= right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid)
            root.right = helper(mid+1, right)

            return root

        return helper(0, len(nums))


if __name__ == '__main__':

    solu = Solution()
    nums = [-10, -3, 0, 5, 9]

    root = solu.sortedArrayToBST(nums)

    print(root.levelOrder())
    assert root.val == 0
