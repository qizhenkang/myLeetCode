# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:17:33 2021

@author: Zhenkang
"""

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        读题：
        1、这题好像见过，“原地哈希”，就自身作为哈希表，实现On和常数空间
        2、这题好像有点不一样，他有一个N，不好处理
        
        测试：
        1、错了一次，发现思路有问题，修改后好了
        
        答案：
        1、有很多种方法，特别是异或和数学，我没仔细看
        """
        N = len(nums)

        for i in range(N):
            while nums[i] != i and nums[i] < N:
                # print(nums[i],i)
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
        
        
        # print(nums)
        for i in range(N):
            if nums[i] != i:
                return i
        
        return N


if __name__ == '__main__':
    solu = Solution()
    arr = [1,3,5,7,8]
    difference = 1
    nums = [9,6,4,2,3,5,7,0,1]
    nums = [1]
    # nums = [2,7,4,5,9,0,6,8,3]
    difference = 0
    # difference = 1
    output_Str = 'result = ' + str(solu.missingNumber(nums))
    print(output_Str)