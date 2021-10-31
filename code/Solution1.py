# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:30:41 2021

@author: qizhe
"""
from typing import List
from collections import defaultdict

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1


if __name__ == '__main__':
    solu = Solution()
    # distance = [2,1,1,2]
    # distance = [1,2,3,4]
    nums = ["Hello","Alaska","Dad","Peace"]
    result = solu.findWords(nums)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)