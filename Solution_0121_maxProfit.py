# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 23:27:00 2021

@author: qizhe
"""

class Solution:
    def maxProfit(self, prices) -> int:
        
        """
        感觉像是一个动态规划的问题，最大利润
        假设i代表的是第i天卖出的最大利润
        """
        
        minPrice = 1e5 
        maxPro = 0
        for p in prices:
            maxPro = max(p - minPrice,maxPro)
            minPrice = min(minPrice,p)
        
        return maxPro

        
        # m = len(prices)
        
        # if m < 2:
        #     return 0
        
        # dp = [0]*m
        
        # maxValue = max(prices[1:])
        # maxValuePosition = prices.index(maxValue)
        # for i in range(m-1):
        #     if i < maxValuePosition:
        #         dp[i] = max(maxValue - prices[i],0)
        #     else:
        #         maxValue = max(prices[i+1:])
        #         maxValuePosition = prices.index(maxValue,i+1)
                
        # print(dp)
        
        # return max(dp)
        
        
        
        
        

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [7,1,5,3,6,4]
    # input_List = [2,1,2,0,1]
    # input_int = 6

    result = solu.maxProfit(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)