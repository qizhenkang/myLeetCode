# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 09:38:14 2021

@author: qizhe
"""

class Solution:
    def findIntegers(self, n: int) -> int:
        """
        越看越像一个DP问题

        Parameters
        ----------
        n : int
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        
        # # 获取最高位数
        # bitCount = -1
        # tempn = n
        # while tempn > 0:
        #     tempn //= 2
        #     bitCount += 1
        
        dp = [0]*30
        
        dp[0] = 1
        dp[1] = 1
        # dp[2] = 1
        
        for i in range(2,len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        
        # print(dp)
            
            
        result = 0
        pre = 0
        
        for i in range(30,-1,-1):
            val = 1 << i 
            if n & val:
                n -= val
                result += dp[i+1]
                if pre:
                    break
                pre = 1
            else:
                pre = 0
            
            if i == 0:
                result += 1
            
        
        return result

        



if __name__ == '__main__':
    solu = Solution()

    # input_Str = str('hello')
    # input_list =
    # input_List = [1]
    input_Num = 9

    # for i in input_List:

    result = solu.findIntegers(input_Num)

    output_Str = ' result = ' + str(result)
    print(output_Str)