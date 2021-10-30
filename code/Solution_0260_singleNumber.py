# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 09:44:04 2021

@author: qizhe
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        读题：
        1、想了半天没想出来，去看答案了
        2、本质上是建立哈希表，不行就排序，这里要求很高，应该是由其他算法
        
        答案：
        1、异或运算
        
        测试：
        1、错了一次，找hotbit出错了，
        2、改错成功，与答案一致了
        """
        # result = []
        orsum = 0
        for n in nums:
            orsum ^= n
            # print(orsum)
        # print(orsum)
        hotbit = orsum & (-orsum)
        print(hotbit)
        hotbit = 0
        # while True:

        #     if orsum%2:
        #         break
        #     orsum >>= 1
        #     hotbit +=1
        #     # print(orsum)
        # print(hotbit)
        x1 = 0
        x2 = 0
        for n in nums:
            if n & hotbit:
                x1 ^=n
            else:
                x2 ^=n
        return [x1,x2]

        

if __name__ == '__main__':
    solu = Solution()
    # distance = [2,1,1,2]
    # distance = [1,2,3,4]
    nums = [1,2,1,3,2,5]
    nums = [43772400,1674008457,1779561093,744132272,1674008457,448610617,1779561093,124075538,-1034600064,49040018,612881857,390719949,-359290212,-812493625,124732,-1361696369,49040018,-145417756,-812493625,2078552599,1568689850,865876872,865876872,-1471385435,1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,124732,661111294,-1813882010,1568689850,448610617,1347212898,-1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,-359290212,1475115274,1793963758,1347212898,43772400,-1471385435,124075538,-1293494866,-119634980,390719949]
    result = solu.singleNumber(nums)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)