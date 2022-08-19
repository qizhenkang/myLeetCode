# -*- coding: utf-8 -*-
"""
Created on 2022/08/19 21:08:29

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


# Definition for singly-linked list.


from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        sortList _summary_

        就是普通排序算法，来个冒泡排序

        超时了，我再想想怎么办 两次了 超时 没想明白 为什么不能用

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """

        # def exchange(p1: ListNode, p2: ListNode, p1_head: ListNode) -> Tuple[ListNode, ListNode, ListNode]:

        #     # temp = p2
        #     p1.next = p2.next
        #     p1_head.next = p2
        #     p2.next = p1
        #     return p1, p2, p1_head

        head_pre = ListNode(0, head)

        length = 0

        p = head
        while p:
            length += 1
            p = p.next

        # print('length = %d' % length)

        for i in range(length):
            cnt = 0
            p0 = head_pre
            p1 = p0.next
            p2 = p1.next
            # print('p1 = %s' % p1.val)
            while cnt < length - i - 1:
                print(cnt)

                # print('p2 = %s' % p2.val)
                if p1.val > p2.val:
                    # exchange
                    # print(p0.val, p1.val, p2.val)
                    p1.next = p2.next
                    p0.next = p2
                    p2.next = p1

                    p1 = p0.next
                    p2 = p1.next
                    # print(p0.val, p1.val, p2.val)

                p0 = p0.next
                p1 = p1.next
                p2 = p2.next

                cnt += 1

        return head_pre.next


if __name__ == '__main__':

    solu = Solution()

    node1 = ListNode(4)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(1)

    head = ListNode(0, node1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    a = solu.sortList(node1)

    while a:
        print(a.val)
        a = a.next
