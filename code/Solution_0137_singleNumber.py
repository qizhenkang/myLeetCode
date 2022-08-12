# -*- coding: utf-8 -*-
"""
Created on 2022/08/12 16:59:11

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        singleNumber _summary_

        题目很容易理解

        哈希表

        2 min 一次通过

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """

        result = 0

        hash_dict = {}

        for i in nums:
            if i in hash_dict:
                hash_dict[i] += 1
            else:
                hash_dict[i] = 1

        for key, val in hash_dict.items():

            if val == 1:
                result = key
                break

        return result


if __name__ == '__main__':
    solu = Solution()
    print(solu.singleNumber([2, 2, 3, 2]))
    print(solu.singleNumber([0, 1, 0, 1, 0, 1, 99]))
