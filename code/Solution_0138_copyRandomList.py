# -*- coding: utf-8 -*-
"""
Created on 2022/08/12 19:37:01

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


# Definition for a Node.
from typing import Dict, List, Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return self.__str__()

    def print(self):
        p = self
        while p:
            print(p.val, p.random)
            p = p.next

        return


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        copyRandomList _summary_

        没看懂题目 难就难在这个 random 指针 让你不知道怎么做到深复制

        第一遍建立映射关系，第二遍修改 random 指针

        搞了半天

        看了答案 这是方案二 由于有 hash 空间复杂度 O(n)

        空间复杂度 O(1) 的方案是 1->1'->2->2'->3->3' 然后再拆分

        Args:
            head (Optional[Node]): _description_

        Returns:
            Optional[Node]: _description_
        """
        if not head:
            return None

        hash_dict: Dict[Node, Node] = {}

        p_old = head
        head_new_pre = Node(0)
        p_new = head_new_pre

        while p_old:
            p_new.next = Node(p_old.val, p_old.next, p_old.random)
            hash_dict[p_old] = p_new.next
            p_new = p_new.next
            p_old = p_old.next

        p_new = head_new_pre.next
        while p_new:
            # print('new: ', p_new.val)
            if p_new.random:
                # print('new: ', p_new.val)
                # print('new.random: ', p_new.random.val)
                p_new.random = hash_dict[p_new.random]

            p_new = p_new.next

        return head_new_pre.next


if __name__ == '__main__':
    node5 = Node(1, None, None)
    node4 = Node(10, node5, node5)
    node3 = Node(11, node4, node4)
    node2 = Node(13, node3, node3)
    node1 = Node(7, node2, node2)

    node4.random = node1

    solu = Solution()
    head = solu.copyRandomList(node1)
    head.print()

    # print(head.print())
