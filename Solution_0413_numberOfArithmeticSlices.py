# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 15:42:04 2021

@author: qizhe
"""

class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        """
        实际上，有一个技巧，就是如果多一个，则多t个，t与当前等差数列长度有关
        """
        
        N = len(nums)
        if N <= 2:
            return 0
        result = 0
        
        d = nums[1]-nums[0]
        t = 0
        for i in range(2,len(nums)):
            if nums[i] - nums[i-1] == d:
                t += 1
            else:
                d = nums[i] - nums[i-1]
                t = 0
            
            result += t
                
        
        return result
    
    
    

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [1]
    input_Num = 5

    # for i in input_List:

    result = solu.numberOfArithmeticSlices(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)