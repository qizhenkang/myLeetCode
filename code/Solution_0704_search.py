# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:50:38 2021

@author: qizhe
"""

class Solution:
    def search(self, nums, target: int) -> int:
        """
        每日一题：二分查找

        Parameters
        ----------
        nums : TYPE
            DESCRIPTION.
        target : int
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """

        result = -1
        
        N = len(nums)

        pl = 0
        pr = N - 1

        if nums[pl] == target:
            return pl
        
        if nums[pr] == target:
            return pr

        aim = 0

        while pl <= pr:
            aim = (pl+pr)//2

            if nums[aim] < target:
                pl = aim + 1
            elif nums[aim] > target:
                pr = aim - 1
            else:
                result = aim
                break

        return result