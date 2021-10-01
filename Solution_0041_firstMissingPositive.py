# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:13:25 2021

@author: qizhe
"""

class Solution:
    def firstMissingPositive(self, nums) -> int:
        """
        题目中要求时间复杂度O(N) AND 空间复杂度O(1)
        没有想出怎么做，看了答案
        答案的思路为“原地哈希”，也就是利用nums自身的O(N)空间
        """
        N = len(nums)
        for i in range(N):
            while 1 <= nums[i] <= N and nums[i] != nums[nums[i]-1]:
                print(nums[i],nums[nums[i]-1])
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        # print(nums)
        return N + 1
        

if __name__ == '__main__':
    solu = Solution()
    
    input_List = [1,6,5,4,3,2,1]
    
    # input_List = 1

    result = solu.firstMissingPositive(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)