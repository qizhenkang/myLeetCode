# -*- coding: utf-8 -*-
"""
Created on 2022/09/15 10:35:34

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        """
        flipLights _summary_

        没完全懂，但感觉上是，可以控制所有、奇数、偶数、奇偶数


        一个找规律的题，前6个灯泡中的4个就可以表示所有状态，所有只有 2**4 种可能

        不是非常懂


        Args:
            n (int): _description_
            presses (int): _description_

        Returns:
            int: _description_
        """
        seen = set()
        for i in range(2**4):
            pressArr = [(i >> j) & 1 for j in range(4)]
            if sum(pressArr) % 2 == presses % 2 and sum(pressArr) <= presses:
                status = pressArr[0] ^ pressArr[1] ^ pressArr[3]
                if n >= 2:
                    status |= (pressArr[0] ^ pressArr[1]) << 1
                if n >= 3:
                    status |= (pressArr[0] ^ pressArr[2]) << 2
                if n >= 4:
                    status |= (pressArr[0] ^ pressArr[1] ^ pressArr[3]) << 3
                seen.add(status)
        return len(seen)


if __name__ == '__main__':

    solu = Solution()

    print(solu.flipLights(1, 1))  # 2
    print(solu.flipLights(2, 1))  # 3
    print(solu.flipLights(123, 11))  # 4
