# -*- coding: utf-8 -*-
"""
Created on 2022/08/15 18:57:48

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List, Tuple

from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        明显是一个搜索，写完就可以做出五子棋游戏了。


        没用哈希表，三层循环，最终导致时间超时了
        """
        n = len(points)
        if n < 3:
            return n  # less than 3, just return it
        ans = 0

        def gcd(a, b) -> int:
            while b != 0:
                a, b = b, a % b  # pythonic way
            return a

        for i in range(n-1):  # loop til last second
            hash_map = defaultdict(lambda: 0)  # set default value to 0
            for j in range(i+1, n):
                a = points[i][1] - points[j][1]
                b = points[i][0] - points[j][0]
                gcd_ab = gcd(a, b)
                key = tuple((a // gcd_ab, b // gcd_ab))
                hash_map[key] += 1
            # find max points algin with point i
            max_alignment = max(hash_map.values())
            ans = max(ans, max_alignment + 1)  # + 1 to add point i
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxPoints([[1, 1]]))
    print(solu.maxPoints([[1, 1], [2, 2], [3, 3]]))
    print(solu.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))

    print(solu.maxPoints([[-6, -1], [3, 1], [12, 3]]))  # 3

    print(solu.maxPoints([[5151, 5150], [0, 0], [5152, 5151]]))  # 2
