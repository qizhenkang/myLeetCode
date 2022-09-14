# -*- coding: utf-8 -*-
"""
Created on 2022/09/14 11:16:31

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        """
        trimMean _summary_

        题目很好理解
            - 给你一个整数数组 arr ，请你删除最小 5% 的数字和最大 5% 的数字后，剩余数字的平均值。

        首先判断最小的 5% 和最大的 5% 然后在范围内的加和

        所以，只需要判断 5% 在哪

        只需要sort 一下，用长度删除就可以了

        一次通过 80%


        Args:
            arr (List[int]): _description_

        Returns:
            float: _description_
        """

        arr.sort()

        length = len(arr)
        num_5 = round(length * 0.05)

        cnt = 0
        for i in range(num_5, length-num_5):
            cnt += arr[i]

        result = cnt / (length-2*num_5)
        return result


if __name__ == '__main__':
    solu = Solution()

    print(solu.trimMean([1, 2, 2, 2, 2, 2, 2, 2,
          2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))  # 2.000
    print(solu.trimMean([6, 2, 7, 5, 1, 2, 0, 3, 10,
          2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]))  # 4.000
    print(solu.trimMean([6, 0, 7, 0, 7, 5, 7,
                         8, 3, 4, 0, 7, 8, 1,
                         6, 8, 1, 1, 2, 4, 8, 1, 9,
                         5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0,
                         6, 10, 8, 2, 3, 4]))  # 4.7778
    print(solu.trimMean([9, 7, 8, 7, 7, 8, 4, 4,
                         6, 8, 8, 7, 6, 8, 8, 9, 2, 6, 0, 0, 1, 10, 8, 6,
                         3, 3, 5, 1, 10, 9, 0, 7, 10, 0, 10, 4, 1, 10, 6,
                         9, 3, 6, 0, 0, 2, 7, 0, 6, 7, 2, 9, 7, 7, 3, 0, 1, 6, 1, 10, 3]))  # 5.2778

    a = [4, 8, 4, 10, 0, 7, 1, 3, 7, 8, 8, 3, 4, 1, 6, 2, 1, 1, 8, 0, 9, 8, 0, 3, 9, 10, 3, 10, 1, 10, 7, 3, 2, 1, 4, 9, 10, 7, 6, 4,
         0, 8, 5, 1, 2, 1, 6, 2, 5, 0, 7, 10, 9, 10, 3, 7, 10, 5, 8, 5, 7, 6, 7, 6, 10, 9, 5, 10, 5, 5, 7, 2, 10, 7, 7, 8, 2, 0, 1, 1]
    print(solu.trimMean(a))  # 5.29167
