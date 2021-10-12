# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:22:56 2021

@author: qizhe
"""

class Solution:
    def plusOne(self, digits):
        stack = []
        num = 0
        for d in digits:
            num *= 10
            num += d

        num += 1
        
        while num > 0:
            stack.append(num % 10)
            num //= 10
        
        return stack[::-1]

if __name__ == '__main__':
    solu = Solution()
    
    input_List = [9,9,9,9]
    result = solu.plusOne(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)