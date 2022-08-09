# -*- coding: utf-8 -*-
"""
Created on 2022/08/09 09:39:40

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        pathSum _summary_

        同样是一个搜索 但需要维护一个栈
            -   深度优先搜索
            -   记忆栈的出栈入栈

        10 min 一次通过 但不是很完善

        Args:
            root (Optional[TreeNode]): _description_
            targetSum (int): _description_

        Returns:
            List[List[int]]: _description_
        """

        result = False

        stack_result: List[List[int]] = []
        stack_cur: List[int] = []

        def search_node(root: TreeNode, count: int) -> bool:
            if not root:
                return False

            stack_cur.append(root.val)

            # print(root.val, count)
            if not root.left and not root.right:
                # 叶子结点
                if count + root.val == targetSum:
                    stack_result.append(stack_cur.copy())
                    stack_cur.pop()
                    return True
                else:
                    stack_cur.pop()
                    return False
            result_left = False
            result_right = False
            result_left = search_node(root.left, count + root.val)
            result_right = search_node(root.right, count + root.val)
            stack_cur.pop()
            return result_left or result_right

        result = search_node(root, 0)
        # print(stack_result)

        return stack_result


if __name__ == '__main__':
    node1 = TreeNode(7, None, None)
    node2 = TreeNode(2, None, None)
    node3 = TreeNode(11, node1, node2)
    node4 = TreeNode(4, node3, None)

    node51 = TreeNode(13, None, None)
    node52 = TreeNode(5, None, None)
    node53 = TreeNode(1, None, None)
    node54 = TreeNode(4, node52, node53)

    node5 = TreeNode(8, node51, node54)
    node6 = TreeNode(5, node4, node5)

    solu = Solution()
    result = solu.pathSum(node6, 22)
    assert result == True

    node1 = TreeNode(3, None, None)
    node2 = TreeNode(2, None, None)
    node3 = TreeNode(1, node1, node2)

    solu = Solution()
    result = solu.pathSum(node3, 5)
    assert result == False
