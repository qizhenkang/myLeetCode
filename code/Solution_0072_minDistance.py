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
        """
        
        return 0


if __name__ == '__main__':
    solu = Solution()
    
    word1 = "horse"
    
    word2 = 'ros'
    # arr = '/home//foo/'
    # arr = '/../'
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # input_List = 1

    result = solu.minDistance(word1,word2)

    output_Str = ' result = ' + str(result)
    print(output_Str)