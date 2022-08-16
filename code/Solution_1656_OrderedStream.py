# -*- coding: utf-8 -*-
"""
Created on 2022/08/16 09:44:03

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self._list: List[str] = ["" for _ in range(n)]
        self._used: List[bool] = [False for _ in range(n)]

    def insert(self, idKey: int, value: str) -> List[str]:
        """
        insert 

        看了半天没看懂题目 是不是就是保存一下

        走神了 20 min 一次通过

        Args:
            idKey (int): _description_
            value (str): _description_

        Returns:
            List[str]: _description_
        """
        self._list[idKey-1] = value
        self._used[idKey-1] = True

        result: List[str] = []

        for i in range(self.ptr-1, self.n):
            if not self._used[i]:
                break
            result.append(self._list[i])
            self.ptr = i+2

        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
if __name__ == '__main__':
    os = OrderedStream(5)
    a = os.insert(3, "ccccc")  # 插入 (3, "ccccc")，返回 []
    b = os.insert(1, "aaaaa")  # 插入 (1, "aaaaa")，返回 ["aaaaa"]
    c = os.insert(2, "bbbbb")  # 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"]
    d = os.insert(5, "eeeee")  # 插入 (5, "eeeee")，返回 []
    e = os.insert(4, "ddddd")  # 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]
