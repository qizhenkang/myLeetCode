# -*- coding: utf-8 -*-
"""
Created on 2022/08/29 10:44:01

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        result = []

        for i in range(n):
            index1 = i
            index2 = i+n
            result.append(nums[index1])
            result.append(nums[index2])

        return result


if __name__ == '__main__':
    solu = Solution()

    nums = [2, 5, 1, 3, 4, 7]
    n = 3

    print(solu.shuffle(nums, n))

    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4

    print(solu.shuffle(nums, n))

    nums = [1, 1, 2, 2]
    n = 2

    print(solu.shuffle(nums, n))
