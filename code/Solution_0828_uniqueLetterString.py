# -*- coding: utf-8 -*-
"""
Created on 2022/09/06 10:36:54

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        uniqueLetterString _summary_

        只需要统计，相同字符的出现位置，然后前后相乘，因为他是在统计字符串中的。

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        index = defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        # print(index)

        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res


if __name__ == '__main__':
    solu = Solution()

    print(solu.uniqueLetterString('LEETCODE'))
