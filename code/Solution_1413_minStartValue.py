# -*- coding: utf-8 -*-
"""
Created on 2022/08/09 14:27:15

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        minStartValue _summary_

        感觉就是一个累加最小值呢 3 min解决

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        cnt = 0
        cnt_min = 0
        for num in nums:
            cnt += num
            cnt_min = min(cnt, cnt_min)
            # print(cnt)
        result = -cnt_min + 1
        return result


if __name__ == '__main__':
    solu = Solution()
    nums = [-3, 2, -3, 4, 2]
    assert 5 == solu.minStartValue(nums)

    nums = [1, 2]
    assert 1 == solu.minStartValue(nums)

    nums = [1, -2, -3]
    assert 5 == solu.minStartValue(nums)
