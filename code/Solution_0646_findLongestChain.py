# -*- coding: utf-8 -*-
"""
Created on 2022/09/03 16:09:13

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        findLongestChain _summary_

        感觉有点复杂，因为要反复的遍历搜索，开头都不知道怎么开头

        有点像“单调栈”

        没想出来 放弃了。 排序后的贪心算法反而是最好的。 也可以动态规划

        答案需要先排序一下。真是的。

        Args:
            pairs (List[List[int]]): _description_

        Returns:
            int: _description_
        """

        cur, res = -1e6, 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if cur < x:
                cur = y
                res += 1
        return res


if __name__ == '__main__':
    solu = Solution()

    print(solu.findLongestChain([[1, 2], [2, 3], [3, 4]]))  # 2
