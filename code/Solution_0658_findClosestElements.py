# -*- coding: utf-8 -*-
"""
Created on 2022/08/25 10:26:20

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        findClosestElements _summary_

        首先二分查找 arr 中的 x 位置，然后再怎么办呢，两个指针依次向前移动

        15 min 没想出来，抄答案了

        核心思想是直接双指针缩小

        Args:
            arr (List[int]): _description_
            k (int): _description_
            x (int): _description_

        Returns:
            List[int]: _description_
        """
        # 排除法（双指针）
        size = len(arr)
        left = 0
        right = size - 1

        # 我们要排除掉 size - k 这么多元素
        remove_nums = size - k
        while remove_nums:
            # 调试语句
            # print(left, right, k)
            # 注意：这里等于号的含义，题目中说，差值相等的时候取小的
            # 因此相等的时候，尽量缩小右边界
            if x - arr[left] <= arr[right] - x:  # 我这个等式已经很对了
                right -= 1
            else:
                left += 1
            remove_nums -= 1
        return arr[left:left + k]


if __name__ == '__main__':
    solu = Solution()

    print(solu.findClosestElements([1], 1, 1))
    print(solu.findClosestElements([1, 2, 3, 4, 5], 4, 2.5))
    print(solu.findClosestElements([1, 2, 3, 4, 5], 4, -1))
