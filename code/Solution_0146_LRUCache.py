# -*- coding: utf-8 -*-
"""
Created on 2022/08/16 20:13:32

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class LRUCache:
    """
    这题比想象的难多了

    看答案没看懂
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._dict = {}
        self._use_list = []

    def get(self, key: int) -> int:
        self._dict.get(key, -1)
        self._use_list.append(key)

    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            self._dict[key] = value

            self._use_list.pop(key)
            self._use_list.append(key)
        elif len(self._dict) < self.capacity:
            self._dict[key] = value

            self._use_list.pop(key)
            self._use_list.append(key)
        else:
            return


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # 缓存是 {1=1}
    lRUCache.put(2, 2)  # 缓存是 {1=1, 2=2}
    lRUCache.get(1)    # 返回 1
    lRUCache.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    lRUCache.get(2)    # 返回 -1 (未找到)
    lRUCache.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    lRUCache.get(1)    # 返回 -1 (未找到)
    lRUCache.get(3)    # 返回 3
    lRUCache.get(4)    # 返回 4
