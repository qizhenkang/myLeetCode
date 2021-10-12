# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:06:45 2021

@author: qizhe
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        晚上看到这个题的，想了一下，动态规划可以做应该
        每个有两个状态，和前面一位一起组成一个字母 or 独自组成一个字母
        """
        # 先写一个列表的
        # 
        
        def get_currentState(cur2):
            
            if cur2[1] == '0':
                x1 = 0
                if cur2 == '10' or cur2 == '20':
                    x2 = 1
                elif cur2 == '*0':
                    x2 = 2
                else:
                    x2 = 0
            elif cur2[1] == '*':
                x1 = 9
                if cur2[0] == '1':
                    # 1*
                    x2 = 9
                elif cur2[0] == '2':
                    # 2*
                    x2 = 6
                elif cur2[0] == '*':
                    x2 = 9 + 6
                else:
                    x2 = 0
            else:
                x1 = 1
                if cur2[0] == '*':
                    if cur2[1] <= '6':
                        x2 = 2
                    else:
                        x2 = 1
                elif cur2[0] == '1':
                    x2 = 1
                elif cur2[0] == '2' and cur2[1] <= '6':
                    x2 = 1
                else:
                    x2 = 0
            
            return x1,x2
            
        
        N = len(s)
        
        if N == 1:
            if s == '*':
                return 9
            elif s == '0':
                return 0
            else:
                return 1
        
        dp = [[0,0] for _ in range(N)] 
        
        # 边界条件
        # 先把前两位考虑清楚，后面的就只需要递归求解了
        if s[0] == '*':
            dp[0][0] = 9
            dp[0][1] = 0
        elif s[0] == '0':
            dp[0][0] = 0
            dp[0][1] = 0
        else:
            dp[0][0] = 1
            dp[0][1] = 0

            
        x1, x2 = get_currentState(s[:2])
        dp[1][0], dp[1][1] = dp[0][0] * x1, x2
        
        
        MaxMod = 1e9+7
        for i in range(2,N):
            x1,x2 = get_currentState(s[i-1:i+1])
                
            dp[i][0] = sum(dp[i-1]) * x1 % MaxMod
            dp[i][1] = sum(dp[i-2]) * x2 % MaxMod

        # print(dp)
        # x = sum(dp[-1])
        # print(dp)
        # print(x)
        
        return int(sum(dp[-1]) % MaxMod)


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('1*2*2627*') # 5544
    input_Str = str('1*2*2627') # 616
    # input_Str = str('1*2*') # 288
    # input_Str = str('1*') # 20
    # input_Str = str('***') # 999
    input_Str = str('*1*1*0') # 404
    input_Str = str('1*6*7*1*9*6*2*9*2*3*3*6*3*2*2*4*') # 307809412
    # input_Str = "1*6*7*1*9*6*2*9*2*3*3*6*3*2*2*" # 972305039
    # input_Str = str("1*6*7*1*9*6*2*9*2*3*3*6*3*2*2*4*7*2*9*6*0*6*4*4*1*6*9*0*5*9*2*5*7*7*0*6*9*7*1*5*5*9*3*0*4*9*2*6*2*5*7*6*1*9*4*5*8*4*7*4*2*7*1*2*1*9*1*3*0*6*")
    # 882201566
    # 0不对应

    result = solu.numDecodings(input_Str)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)