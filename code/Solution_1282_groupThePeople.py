# -*- coding: utf-8 -*-
"""
Created on 2022/08/12 08:51:11

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        groupThePeople _summary_

        要求懂了，但是考点没懂

        必然有解，然后其实就是相同数字的在一起，且确定合适的分组

        可能会出现多次遍历的问题，想想怎么办可以减小时间复杂度，最好是哈希对吧

        10 min 一次通过 我的方案是一次生成，这样有点慢

        思路有点不太好，确实是 hash  + hash 后加入表

        Args:
            groupSizes (List[int]): _description_

        Returns:
            List[List[int]]: _description_
        """

        result: List[List[int]] = []

        result_sizes: List[int] = []

        for i, size in enumerate(groupSizes):
            for j, aim_size in enumerate(result_sizes):
                if size == aim_size and len(result[j]) < aim_size:
                    result[j].append(i)
                    break
            else:
                result.append([i])
                result_sizes.append(size)

        return result


if __name__ == '__main__':
    solu = Solution()

    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(solu.groupThePeople(groupSizes))

    groupSizes = [2, 1, 3, 3, 3, 2]
    print(solu.groupThePeople(groupSizes))

    groupSizes = []
    print(solu.groupThePeople(groupSizes))

    groupSizes = [1]
    print(solu.groupThePeople(groupSizes))

    groupSizes = [2, 2]
    print(solu.groupThePeople(groupSizes))
