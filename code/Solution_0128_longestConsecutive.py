# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:37:27 2021

@author: Zhenkang
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        
        这是leetcode第一个并查集的题目，试一下
        
        读题：
        1、最好是排序一下，但时间要求高，怎么办呢
        2、肯定是要牺牲空间，好像是需要搞一个树，是吧，然后最后一下得到
        3、哈希表行不行？感觉也行啊
        
        测试：
        1、搞了一个哈希表，错了测试了两次，出错了
        
        答案：
        1、
        """

        longest_streak = 0
        # 搞成set，这样方便查找
        num_set = set(nums)

        for num in num_set:
            # 只找开头，否则跳过，这样防止重复
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                # 向下找，看能有多长
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                # 记录最长，跳过
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

if __name__ == '__main__':
    solu = Solution()
    heightMap = [9,1,4,7,3,-1,0,5,8,-1,6]
    output_Str = 'result = ' + str(solu.longestConsecutive(heightMap))
    print(output_Str)

    