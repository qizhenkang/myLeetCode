# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 11:20:30 2021

@author: qizhe
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:45:37 2021

@author: qizhe
"""

class Solution:
    def maxProfit(self, prices) -> int:
        
        """
        这个参考答案了，要求最多2次交易，用动态规划来做
        共5种状态
        效果很好，但是没太懂其实，为什么可以这样做，好像是用“状态”；来理解
        这里的状态是，第i天为……状态的最大利润
        """
        
        # 第0天结束时的状态，边界条件
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1,len(prices)):
            buy1 = max(buy1,-prices[i]) # 本质上是在记录当前的最小值
            sell1 = max(sell1,buy1+prices[i]) # 本质上是在记录交易最大利润
            buy2 = max(buy2,sell1-prices[i]) # 
            sell2 = max(sell2,buy2+prices[i])
            print(buy1,sell1,buy2,sell2)

        return sell2
        
        
        

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [3,3,5,0,0,3,1,4,1,1,1]
    # input_List = [[-10]]
    # input_int = 6

    result = solu.maxProfit(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)