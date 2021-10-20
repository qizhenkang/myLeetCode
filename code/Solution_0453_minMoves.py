# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:43:57 2021

@author: qizhe
"""
from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        读题:
        1、这题很有特点啊，n-1个增加1，就等于1个减少1
        2、其实就是把所有的减到最小
        
        测试：
        1、一次通过，性能不错
        """
        minNum = nums[0]
        SumNum = 0
        N = len(nums)
        for i in range(N):
            if minNum > nums[i]:
                minNum = nums[i]
            SumNum += nums[i]
        
        return SumNum - minNum * N
        
        # return sum(nums) - min(nums) * len(nums)

if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]
    n = 8
    inputList = [1,2,3]
    # time = 3
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","cot",'cog']
    # wordList = ["hot","dot","dog","lot","log","cog"]
    # beginWord = "a"
    # endWord = "c"
    # wordList = ["a","b","c"]
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.minMoves(inputList)

    output_Str = ' result = ' + str(result)
    print(output_Str)