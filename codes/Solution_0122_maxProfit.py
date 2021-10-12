# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:45:37 2021

@author: qizhe
"""

class Solution:
    def maxProfit(self, prices) -> int:
        
        """
        第一反应，像是找到所有的上升段，然后卖掉，贪心算法？正确
        
        答案还有一种思路，动态规划，我来试试
        """
        
        # dp0 = 0
        # dp1 = - prices[0]
        # dp0new = 0
        # # dp1new = 0
        # for i in range(1,len(prices)):
        #     dp0 = max(dp0new,dp1 + prices[i])
        #     dp1 = max(dp0new - prices[i],dp1)
        #     dp0new = dp0
        #     # dp1new = dp1
        # return dp0
        # 记录当前状态，若0则等待买入，若1则等待卖出
        state = False
        # 若持有，则偷看明天走势，若涨则按兵不动，若跌则果断卖出
        # 若未持有，则偷看明天走势，若涨则果断买入，若跌则按兵不动
        rise = False
        
        price = 0
        profit = 0
        # prev = 1e6
        N = len(prices)
        for i in range(N):
            
            # 判断涨跌
            if i < N-1:
                if prices[i] < prices[i+1]:
                    rise = True
                else:
                    rise = False
            else:
                # 最后一天，明天肯定不涨了
                rise = False
            
            # 根据状态确定动作
            if state:
                if not rise:
                    profit += prices[i] - price
                    state = False
            else:
                if rise:
                    price = prices[i]
                    state = True
        
        
        return profit
        
        
        

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [7,1,5,6]
    # input_List = [[-10]]
    # input_int = 6

    result = solu.maxProfit(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)