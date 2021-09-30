# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:17:55 2021

@author: qizhe
"""

class Solution:
    def rob(self, nums) -> int:
        
        def robNorm(start,end):
            cur = prev = 0
            for i in nums[start:end]:
                cur, prev = max(cur ,prev+i), cur
            return cur
            
        
        N = len(nums)
        if N <= 2:
            return max(nums)
        else:
            return max(robNorm(0,N-1),robNorm(1,N))
        
        
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [1,2,3]
    # input_List = [[-10]]
    # input_int = 6

    result = solu.rob(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)