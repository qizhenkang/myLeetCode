# -*- coding: utf-8 -*-
"""
Created on 2022/08/13 16:06:02

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x, next: 'ListNode'):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        hasCycle _summary_

        快慢指针

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            bool: _description_
        """
        p_fast, p_slow = head, head
        while True:
            if not (p_fast and p_fast.next):
                return
            p_fast, p_slow = p_fast.next.next, p_slow.next
            if p_fast == p_slow:
                break
        p_fast = head
        while p_fast != p_slow:
            p_fast, p_slow = p_fast.next, p_slow.next
        return p_fast


if __name__ == '__main__':
    node1 = ListNode(-4, None)
    node2 = ListNode(0, node1)
    node3 = ListNode(2, node2)
    node4 = ListNode(3, node3)

    node1.next = node3

    solu = Solution()
    print('result:', solu.detectCycle(node4).val)
