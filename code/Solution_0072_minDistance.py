# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:21:05 2021

@author: qizhe
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        读题：
        1、看了几分钟，没什么好思路
        2、看了提示，提示动态规划，好像是应该动态规划，但还是没什么好思路
        3、动态规划好像应该找状态转移
        
        二次读题：
        1、能不能前i个和前j个的最小，然后逐步更新？
        2、目前还有问题，回来再做，感觉差不多了的
        
        测试：
        1、一次通过了，性能还行
        2、其实没有完全懂，猜出来了他的表达方式
        
        答案：
        1、看了答案，确实是这个意思，也就是 n-1 问题到 n 问题，那最小就是+1呀
        """
        m = len(word1)
        n = len(word2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 0
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

        return dp


if __name__ == '__main__':
    solu = Solution()
    
    word1 = "horse"
    word2 = 'ros'
    word1 = "inten"
    word2 = "execu"
    word1 = "abcde"
    word2 = "adcb"
    # arr = '/home//foo/'
    # arr = '/../'
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # input_List = 1

    result = solu.minDistance(word1,word2)
    for i in result:
        print(i)
    # output_Str = ' result = ' + str(result)
    # print(output_Str)