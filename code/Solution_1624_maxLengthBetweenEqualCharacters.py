# -*- coding: utf-8 -*-
"""
Created on 2022/09/17 09:31:34

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        maxLengthBetweenEqualCharacters _summary_

        两个相同字符之间的最长字符串

        感觉需要暴力双指针呢

        10 min 2 次通过 开着会做的 错了一次

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """

        # p1 = 0

        max_length = -1
        for p1 in range(len(s)):
            p2 = len(s)-1
            while p1 < p2 and p2-p1 > max_length:
                if s[p1] == s[p2]:
                    max_length = max(max_length, p2-p1-1)
                    break
                # p1 += 1
                p2 -= 1

        return max_length


if __name__ == '__main__':
    solu = Solution()

    print(solu.maxLengthBetweenEqualCharacters("aa"))  # 0
    print(solu.maxLengthBetweenEqualCharacters("abca"))  # 2
    print(solu.maxLengthBetweenEqualCharacters("cbzxy"))  # -1
    print(solu.maxLengthBetweenEqualCharacters("cabbac"))  # 4
    print(solu.maxLengthBetweenEqualCharacters("scayofdzca"))  # 6
