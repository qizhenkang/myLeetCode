# -*- coding: utf-8 -*-
"""
Created on 2022/08/12 16:50:10

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        singleNumber _summary_

        题目很容易理解，但不确定如何写效率高，是不是有异或在这？

        4 min 一次通过 全部异或一下结束了

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """

        result = 0
        for i in nums:
            result ^= i
        return result


if __name__ == '__main__':
    solu = Solution()
    print(solu.singleNumber([2, 2, 1]))
    print(solu.singleNumber([4, 1, 2, 1, 2]))
