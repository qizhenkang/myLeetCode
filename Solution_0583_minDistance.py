# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:12:34 2021

@author: qizhe
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        # print(dp)
        return m + n - 2 * dp[m][n]


if __name__ == '__main__':
    solu = Solution()

    # input_List = Node(1,None,None,None)

    result = solu.minDistance('ab', 'ebcda')

    output_Str = ' result = ' + str(result)
    print(output_Str)