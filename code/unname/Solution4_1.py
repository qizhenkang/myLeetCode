# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 16:05:41 2021

@author: qizhe
"""

# import string
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        """
        感觉不难：
        1、对比的是数字长度
        2、简单的正则表达
        3、回溯即可
        """
        m = len(s1)
        n = len(s2)
        dp = [[False]*(n+1) for _ in range(m+1)]
        
        dp[0][0] = True
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if 'a' <= s1[i] <= 'z' and 'a' <= s2[j] <= 'z':
        #             dp[i][j] = dp[i-1][j-1] if s1[i] == s2[j] else False
        #         else:
        #             if 'a' <= s1[i] <= 'z':
                        

                

        return False
    
if __name__ == '__main__':
    solu = Solution()
    # distance = [2,1,1,2]
    # distance = [1,2,3,4]
    # nums = ["Hello","Alaska","Dad","Peace"]
    
    nums = [1,3]
    start = 6
    goal = 4
    
    s1 = "internationalization"
    s2 = "i18n"

    result = solu.possiblyEquals(s1,s2)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)