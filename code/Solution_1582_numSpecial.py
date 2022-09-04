# -*- coding: utf-8 -*-
"""
Created on 2022/09/04 10:52:17

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        第一遍没做出来 抄答案了

        核心思想是先统计出来个数 然后遍历

        我只统计了个数

        """

        rows_sum = [sum(row) for row in mat]
        cols_sum = [sum(col) for col in zip(*mat)]
        res = 0
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                if x == 1 and rows_sum[i] == 1 and cols_sum[j] == 1:
                    res += 1
        return res
