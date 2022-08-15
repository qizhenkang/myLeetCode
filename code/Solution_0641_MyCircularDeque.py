# -*- coding: utf-8 -*-
"""
Created on 2022/08/15 10:51:47

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class MyCircularDeque:
    """

    虽然 10 min  一次通过
    这题的理解其实有点错误，不应该用 list 的函数， 而应该只用数组的下标来实现\

        又花了 15 min 重新用数组写了一下
    """

    def __init__(self, k: int):
        self.max_length = k
        self._list: List[int] = [0 for _ in range(k)]

        self._front: int = 0
        self._rear: int = 0
        self._empty = True
        self._full = False if k else True

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self._front -= 1
        self._front %= self.max_length
        self._list[self._front] = value

        self._empty = False
        if self._front == self._rear:
            self._full = True
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self._list[self._rear] = value
        self._rear += 1
        self._rear %= self.max_length

        self._empty = False
        if self._front == self._rear:
            self._full = True
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._front += 1
        self._front %= self.max_length

        self._full = False
        if self._front == self._rear:
            self._empty = True
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self._rear -= 1
        self._rear %= self.max_length

        self._full = False
        if self._front == self._rear:
            self._empty = True
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self._list[self._front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self._list[(self._rear-1) % self.max_length]

    def isEmpty(self) -> bool:
        return self._empty

    def isFull(self) -> bool:
        return self._full


if __name__ == '__main__':
    # Your MyCircularDeque object will be instantiated and called as such:
    obj = MyCircularDeque(3)
    # print(obj._list)
    # param_1 = obj.insertFront(1)
    # print(obj._list)
    # param_1 = obj.insertFront(2)
    # print(obj._list)
    # param_1 = obj.insertFront(3)
    # print(obj._list)
    # param_2 = obj.insertLast(4)
    # print(obj._list, param_2)
    # param_3 = obj.deleteFront()
    # print(obj._list, param_3)
    # param_4 = obj.deleteLast()
    # print(obj._list)
    # param_5 = obj.getFront()
    # print(param_5)
    # param_6 = obj.getRear()
    # print(param_6)
    # param_7 = obj.isEmpty()
    # param_8 = obj.isFull()

    obj.insertLast(1)			        # 返回 true
    obj.insertLast(2)			        # 返回 true
    obj.insertFront(3)			        # 返回 true
    obj.insertFront(4)			        # 已经满了，返回 false
    obj.getRear()  				# 返回 2
    obj.isFull()				        # 返回 true
    obj.deleteLast()			        # 返回 true
    obj.insertFront(4)			        # 返回 true
    print(obj._list, obj._front)
    obj.getFront()				# 返回 4
