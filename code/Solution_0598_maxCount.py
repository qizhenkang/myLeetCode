# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 10:18:06 2021

@author: Zhenkang
"""
from typing import List
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minX = m
        minY = n
        for op in ops:
            minX = min(op[0],minX)
            minY = min(op[1],minY)
        return minX * minY