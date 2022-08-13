# -*- coding: utf-8 -*-
"""
Created on 2022/08/13 15:48:15

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        hasCycle _summary_

        快慢指针

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            bool: _description_
        """
        if not head or not head.next:
            return False
        p_slow = head
        p_fast = head.next

        while p_slow and p_fast and p_fast.next:
            if p_slow == p_fast:
                return True
            p_slow = p_slow.next
            p_fast = p_fast.next.next

        return False


if __name__ == '__main__':
    node1 = ListNode(-4, None)
    node2 = ListNode(0, node1)
    node3 = ListNode(2, node2)
    node4 = ListNode(3, node3)

    node1.next = node3

    solu = Solution()
    print(solu.hasCycle(node4))
