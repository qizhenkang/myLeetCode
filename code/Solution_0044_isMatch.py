# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:36:38 2021

@author: qizhe
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        读题：
        1、和之前10.正则表达式很像，'？'就是'.'
        2、不同点在于，这里的'*'匹配的是任意字符串，这意味着，不需要判断匹配
        3、动态规划来做，定义是前i个和前j个是否匹配
        
        测试：
        1、出了一点小问题，一次通过，20min，但性能不好
        
        答案：
        1、与答案思路一一致
        2、可以用贪心算法这个题，因为'*'不与前面字符相关，其实就是匹配字符串
        
        但总感觉还没有完全理解
        """
        m = len(s)
        n = len(p)
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    # print(i,j)
                    dp[i][j] |= dp[i-1][j] | dp[i][j-1] 
                else:
                    if p[j-1] == '?' or i > 0 and s[i-1] == p[j-1]:
                        dp[i][j] |= dp[i-1][j-1] if i > 0 else False
        return dp




if __name__ == '__main__':
    solu = Solution()
    
    
    # input_Str_s = "aaacd"
    # input_Str_p = "a*aaaacd"
    # input_Str_s = str('mississippi')
    # input_Str_p = str('mis*is*p*.')
    
    input_Str_s = str('abcdef')
    input_Str_p = str('*')
    
    # input_Str_s = str('a')
    # input_Str_p = str('a*b*c*')
    
    # input_Str_s = str('aa')
    # input_Str_p = str('a')
    result = solu.isMatch(input_Str_s, input_Str_p)
    for i in result:
        print(i)
    
    # output_Str = 'result = ' + str(result)
    # print(output_Str)
