# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:50:45 2021

@author: qizhe
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while n and n % 3 == 0:
            n //= 3
        
        return n == 1
            
        
        
        # if n == 1:
        #     return True
        
        # if n < 3:
        #     return False
        
        # while True :
            
        #     if n == 3:
        #         break
        #     n = n / 3
            
        #     if n != int(n):
        #         # print(n)
        #         return False
        
        # return True
        
        


if __name__ == '__main__':
    solu = Solution()
    
    input_List = 1
    
    result = solu.isPowerOfThree(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)