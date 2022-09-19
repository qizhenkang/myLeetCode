# -*- coding: utf-8 -*-
"""
Created on 2022/09/19 10:48:37

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        frequencySort _summary_

        统计频率，按频率升序

        同频率，按数字降序大小

        一次通过 20 min

        然后看答案发现可以非常简单

        根据这个题目学会了 Counter 和 sort 的用法

        Args:
            nums (List[int]): _description_

        Returns:
            List[int]: _description_
        """

        # 统计频率
        from collections import Counter
        nums_freq = Counter(nums)

        # 按照要求排序
        # 这个原地排序很高级的
        nums.sort(key=lambda x: (nums_freq[x], -x))

        return nums


if __name__ == '__main__':

    solu = Solution()

    print(solu.frequencySort([1, 1, 2, 2, 2, 3]))  # [3,1,1,2,2,2]
    print(solu.frequencySort([2, 3, 1, 3, 2]))  # [1,3,3,2,2]
    # [5,-1,4,4,-6,-6,1,1,1]
    print(solu.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
    print(solu.frequencySort([1, 2]))  # []

    print(solu.frequencySort([2, 3, 1, 3, 2]))  # [1,3,3,2,2]
