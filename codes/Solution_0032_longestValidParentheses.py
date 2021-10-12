# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:56:27 2021

@author: qizhe
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        按照动态规划的思路，需要建立状态转移方程
        他要找的是当前的最长匹配括号
        那么，我需要找的是，前n个字符的最长匹配
        """
        l = len(s)
        nowLen = 0
        maxLen = 0
        stack = [-1]
        for i in range(l):
            if s[i] == '(':
                # 栈记录下标
                stack.append(i)
            else:
                # if stack:
                stack.pop()
                if stack:
                    nowLen = i - stack[-1]
                    maxLen = max(maxLen,nowLen)
                else:
                    # 记录最后一个未被匹配的右括号
                    stack.append(i)
        return maxLen
                    

        
        # l = len(s)
        # stack = 0
        # dp = [0] * l
        # # dp定义为前i个字符的最长匹配子串长度
        # for i in range(l):
            
        #     if s[i] == '(':
        #         dp[i] = dp[i-1]
        #         stack += 1
        #     else:
        #         if stack:
        #             stack -= 1
        #             dp[i] = dp[i-1] + 2
        #         else:
        #             dp[i] = dp[i-1]
        #             stack = 0
        # print(dp)
        # return maxLen
    
if __name__ == '__main__':
    solu = Solution()

    # input_Str = str('))()()')
    # input_Str = str('()(()')
    # input_Str = str(')()())')
    input_Str = str('(()')
    # input_list =
    input_List = [1,3,5]
    input_int = 1

    result = solu.longestValidParentheses(input_Str)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)