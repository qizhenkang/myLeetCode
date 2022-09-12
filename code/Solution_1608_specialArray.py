# -*- coding: utf-8 -*-
"""
Created on 2022/09/12 17:04:09

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        specialArray _summary_

        15 min 2次通过，错了一次，是因为写的条件不是非常清楚 与答案思路一致

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """

        nums.sort(reverse=True)

        length = len(nums)

        for i, n in enumerate(nums):

            if i < length-1 and nums[i] >= i+1 and nums[i] > nums[i+1] and nums[i+1] < i+1:
                # print(i, nums[i], nums[i+1])
                return i+1
            elif i == length-1 and nums[i] >= i+1:
                return i+1

        return -1


if __name__ == '__main__':
    solu = Solution()

    print(solu.specialArray([3, 5]))  # 2
    print(solu.specialArray([0, 0]))  # -1
    print(solu.specialArray([0, 4, 3, 0, 4]))  # 3
    print(solu.specialArray([3, 6, 7, 7, 0]))  # -1
    print(solu.specialArray([5, 5, 5, 5, 5]))  # 5
