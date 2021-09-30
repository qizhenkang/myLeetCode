# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:54:41 2021

@author: qizhe
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        暴力解 -> 二分查找
        """
        # i = 0
        # while i < 46342:
        #     if i * i > x:
        #         return i-1
        #     i += 1
        
        # return i
        
        """
        牛顿迭代法
        """
        if x == 0:
            return 0
        x0 = x
        error = 1.0e9
        while abs(error) > 1e-3:
            error = x0 * x0 - x
            x0 = x0 - error / (2 * x0)
        
        return int(x0)

        


if __name__ == '__main__':
    solu = Solution()
    
    num = 2147395600
    
    result = solu.mySqrt(num)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)