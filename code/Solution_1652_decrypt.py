# -*- coding: utf-8 -*-
"""
Created on 2022/09/24 15:48:00

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        decrypt _summary_

        和炸弹完全没关系。

        简单模拟一下，指针即可.


        用时 7 min 一次通过，未 debug

        Args:
            code (List[int]): _description_
            k (int): _description_

        Returns:
            List[int]: _description_
        """

        length = len(code)
        result = [0 for _ in range(length)]

        if k > 0:
            for i in range(length):
                temp = 0
                cnt = 0
                # 循环 == 滑动窗口+指针取模
                # 可以去掉循环，把code加倍来做
                while cnt < k:
                    temp += code[(i+cnt+1) % length]
                    cnt += 1
                result[i] = temp
        elif k < 0:
            for i in range(length):
                temp = 0
                cnt = 0
                while cnt < abs(k):
                    temp += code[(i-cnt-1) % length]
                    cnt += 1
                result[i] = temp

        return result


if __name__ == '__main__':
    solu = Solution()

    print(solu.decrypt([5, 7, 1, 4], 3))  # [12,10,16,13]
    print(solu.decrypt([1, 2, 3, 4], 0))  # [0,0,0,0]
    print(solu.decrypt([2, 4, 9, 3], -2))  # [12,5,6,13]
