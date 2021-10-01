# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:43:49 2021

@author: qizhe
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        第一思路以为是转换为整数
        在看了一眼题，应该是让实现整数乘法?
        """
        
        number1 = 0
        number2 = 0
        
        for i in range(len(num1)):
            number1 = number1 * 10 + int(num1[i])
        for i in range(len(num2)):
            number2 = number2 * 10 + int(num2[i])
        
        
        return str(number1*number2)
        
        
        
        
        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = [1,6,5,4,3,2,1]
    
    # input_List = 1

    result = solu.multiply('123','456')

    output_Str = ' result = ' + str(result)
    print(output_Str)