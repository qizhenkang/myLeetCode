# -*- coding: utf-8 -*-
"""
Created on 2022/08/26 16:26:33

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        maxProduct _summary_

        找最大值和次大值，然后乘一下

        6 min 2 次成功

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """

        if nums[0] > nums[1]:
            n_max1 = nums[0]
            n_max2 = nums[1]
        else:
            n_max1 = nums[1]
            n_max2 = nums[0]

        for n in nums[2:]:
            if n >= n_max1:
                n_max2 = n_max1
                n_max1 = n
            elif n_max2 <= n and n < n_max1:
                n_max2 = n

        return (n_max1-1) * (n_max2-1)


if __name__ == '__main__':

    solu = Solution()
    print(solu.maxProduct([3, 4, 5, 2]))
    print(solu.maxProduct([3, 7]))
