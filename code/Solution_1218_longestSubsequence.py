# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:49:36 2021

@author: Zhenkang
"""
from typing import List
from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        读题：
        1、感觉就是一个并查集，找最长子序列嘛
        2、感觉有点问题是，他要求要子序列，他也就是要考虑顺序
        3、试试最简单的思路
        
        感觉好麻烦啊，应该是没有找到合适的思路
        答案：
        1、竟然是动态规划
        
        """
        # 哈希表dp，有点意思，第一次见到
        # 你看这里的用法，int一下就把初始化为0了
        dp = defaultdict(int)
        for v in arr:
            # 这里自然地考虑了子序列，之前没出现过就是0，出现过就+1
            dp[v] = dp[v - difference] + 1
        
        return max(dp.values())
    

if __name__ == '__main__':
    solu = Solution()
    arr = [1,3,5,7,8]
    difference = 1
    arr = [4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8]
    difference = 0
    # difference = 1
    output_Str = 'result = ' + str(solu.longestSubsequence(arr,difference))
    print(output_Str)
