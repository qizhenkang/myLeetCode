# -*- coding: utf-8 -*-
"""
Created on 2022/09/23 10:03:23

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Node:
    def __init__(self, val: int, next: 'Node' = None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    """
    MyLinkedList

    15 min 一次通过

    和答案中的单相链表如出一辙，几乎是完全一样

    """

    def __init__(self):
        self.head_pre = Node(-1)
        self._length = 0

    def get(self, index: int) -> int:
        if index >= self._length:
            return -1

        temp = self.head_pre
        for _ in range(index+1):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head_pre.next)
        self.head_pre.next = node
        self._length += 1
        return

    def addAtTail(self, val: int) -> None:
        temp = self.head_pre
        while temp.next:
            temp = temp.next
        temp.next = Node(val)
        self._length += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index > self._length:
            return
        else:  # 0 < index <= len(self._length)
            temp = self.head_pre
            for _ in range(index):  # 找第 index -1 个
                temp = temp.next

            node = Node(val, temp.next)
            temp.next = node
            self._length += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._length:
            return
        else:  # 0 <= index < len(self._length)
            temp = self.head_pre
            for _ in range(index):  # 找第 index -1 个
                temp = temp.next

            temp.next = temp.next.next
            self._length -= 1
        return

    def _show(self):
        temp = self.head_pre.next
        while temp:
            print(temp.val, end='->')
            temp = temp.next
        print('END')
        return

    # def _get_node(self, index: int) -> Node:

    #     if index < 0 or index >= self._length:
    #         return None
    #     temp = self.head_pre
    #     for _ in range(index+1):
    #         temp = temp.next
    #     return temp


if __name__ == '__main__':
    # pass
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    param_1 = obj.get(0)
    param_2 = obj.addAtHead(1)
    param_3 = obj.addAtTail(3)
    param_4 = obj.addAtIndex(2, 2)
    obj._show()
    param_5 = obj.get(1)  # 2
    param_6 = obj.deleteAtIndex(1)
    param_6 = obj.deleteAtIndex(1)
    param_6 = obj.deleteAtIndex(1)
    param_7 = obj.get(1)  # 3
    param_6 = obj.deleteAtIndex(0)
    obj._show()
    # obj.deleteAtIndex(index)
