# -*- coding: utf-8 -*-
"""
Created on 2022/09/10 18:20:57

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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        trimBST _summary_

        如果 N 节点越下界，那他的左子树都不应该要了，然后把右子树放在新节点
        如果 N 节点越上界，那他的右子树都不应该要了，然后把左子树放在新节点

        错误了一次，是因为根节点处理不好

        为了防止错误，加入了一个 parent 的 left or right 标识，用来标识 这个节点是原来的左还是右

        这样越界之后，只需要对应的修改即可

        答案高级，直接 dfs 一步到位

        Args:
            root (Optional[TreeNode]): _description_
            low (int): _description_
            high (int): _description_

        Returns:
            Optional[TreeNode]: _description_
        """

        def dfs(node: TreeNode, parent: TreeNode, left_right: int):
            if not node:
                return

            if node.val < low or node.val > high:
                if node.val < low:
                    new_node = node.right
                else:
                    new_node = node.left

                if left_right == 0:
                    parent.left = new_node
                    dfs(parent.left, parent, 0)
                else:
                    parent.right = new_node
                    dfs(parent.right, parent, 1)
            else:
                dfs(node.left, node, 0)
                dfs(node.right, node, 1)

            return

        pre = TreeNode()
        pre.left = root

        dfs(root, pre, 0)

        return pre.left


if __name__ == '__main__':
    solu = Solution()

    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node2.left = node1
    node0.right = node2
    node3.left = node0
    node3.right = node4

    root = solu.trimBST(node3, 1, 3)

    print(root.levelOrder())

    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)

    node1.left = node0
    node1.right = node2

    root = solu.trimBST(node1, 1, 2)
    print(root.levelOrder())

    node3 = TreeNode(3)

    root = solu.trimBST(node3, 2, 2)
    print(root.levelOrder())
