# -*- coding: utf-8 -*-
"""
Created on 2022/08/18 19:10:47

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        """
        maxEqualFreq _summary_

        没有做出来

        有一个关键的东西，是频率的频率，啊这

        两种情况:
            -   一种是 333 1
                -   最大和1
            -   一种是 333 4
                -   次大 和 最大

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """

        from collections import Counter
        freq, count = Counter(), Counter()
        ans = maxFreq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            maxFreq = max(maxFreq, count[num])
            freq[count[num]] += 1
            if maxFreq == 1 or \
               freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == i + 1 and freq[maxFreq] == 1 or \
               freq[maxFreq] * maxFreq + 1 == i + 1 and freq[1] == 1:
                ans = max(ans, i + 1)
        return ans


if __name__ == '__main__':
    solu = Solution()

    print(solu.maxEqualFreq([2, 2, 1, 1, 5, 3, 3, 5]))
    print(solu.maxEqualFreq([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]))
