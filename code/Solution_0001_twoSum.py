# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:16:39 2021

@author: qizhe
"""
from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        读题：
        1、想用双指针，但好像没排序
        
        答案：
        1、哈希表，不断加入
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    nums = [2,7,11,15]
    target = 9

    result = solu.twoSum(nums,target)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)