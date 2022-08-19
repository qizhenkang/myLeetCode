# -*- coding: utf-8 -*-
"""
Created on 2022/08/19 10:56:16

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        result = 0

        for s, e in zip(startTime, endTime):

            if s <= queryTime and queryTime <= e:
                result += 1

        return result


if __name__ == '__main__':
    pass
    solu = Solution()

    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4

    print(solu.busyStudent(startTime, endTime, queryTime))

    startTime = [4]
    endTime = [4]
    queryTime = 4

    print(solu.busyStudent(startTime, endTime, queryTime))

    startTime = [4]
    endTime = [4]
    queryTime = 5

    print(solu.busyStudent(startTime, endTime, queryTime))

    startTime = [1, 1, 1, 1]
    endTime = [1, 3, 2, 4]
    queryTime = 7

    print(solu.busyStudent(startTime, endTime, queryTime))

    startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    queryTime = 5

    print(solu.busyStudent(startTime, endTime, queryTime))
