# -*- coding: utf-8 -*-
"""
Created on 2022/08/10 15:51:19

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        sortedListToBST _summary_

        没想到什么好办法，链表不如列表灵活

        看了一下答案，又是去找链表的中点，啊这

        完全不懂。。抄答案默写了一下，基本的思路依然是找中点

        但是需要找 head 到 None 的中点 是我没有想到的

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[TreeNode]: _description_
        """

        def get_median(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def binary_tree(left: ListNode, right: ListNode) -> TreeNode:

            if left == right:
                return None

            median = get_median(left, right)
            root = TreeNode(median.val)

            # print(left.val, right.val, median.val)

            root.left = binary_tree(left, median)
            root.right = binary_tree(median.next, right)

            return root

        if not head:
            return None
        right = head
        while right.next:
            right = right.next
        # print(right.val)

        return binary_tree(head, None)


if __name__ == '__main__':
    solu = Solution()
    node5 = ListNode(9, None)
    node4 = ListNode(5, node5)
    node3 = ListNode(0, node4)
    node2 = ListNode(-3, node3)
    node1 = ListNode(-10, node2)

    root = solu.sortedListToBST(node1)

    print(root.levelOrder())
    # assert root.val == 0
