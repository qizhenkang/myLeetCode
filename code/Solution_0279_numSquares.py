# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:28:10 2021

@author: qizhe
"""
import math
class Solution:
    def numSquares(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        if math.floor(math.sqrt(n))**2 == n:
            return 1
        
        
        result = [n] * (n+1)
        result[0] = 0
        # result[1] = 1
        for i in range(1,n+1):
            for j in range(1,math.floor(math.sqrt(i) + 1)):
                # print(i,j,result[i])
                result[i] = min(result[i],result[i-j*j] + 1)
        
        return result[n]
    
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [1]
    input_Num = 12

    # for i in input_List:

    result = solu.numSquares(input_Num)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)