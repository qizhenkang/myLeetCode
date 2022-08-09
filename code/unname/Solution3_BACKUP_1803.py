# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:43:43 2021

@author: qizhe
"""

from typing import List
from collections import defaultdict

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        """
        最短路径问题，BFS吧
        """
        
        stack = [start]
        depth = 0
        memo = set()
        resultFlag = 0
        result = -1
        while stack:
            # print(stack)
            # print(depth)
            num = len(stack)
            for i in range(num):
                x = stack.pop(0)
                memo.add(x)
                if x == goal:
                    # print('goal',depth)
                    return depth
                if x > 1000 or x < 0:
                    continue
                for n in nums:
                    num1 = x+n
                    num2 = x-n
                    num3 = x^n
                    # print(num1,num2,num3)
                    if num1 not in memo:
                        if num1 > 1000 or num1 <0:
                            if num1 == goal:
                                # print('goal1',depth)
                                result = depth + 1
                                resultFlag = 1
                                # return depth + 1
                        else:
                            stack.append(num1)
                            memo.add(num1)
                    if num2 not in memo:
                        if num2 > 1000 or num2 <0:
                            if num2 == goal:
                                # print('goal2',depth)
                                result = depth + 1
                                resultFlag = 1
                        else:
                            stack.append(num2)
                            memo.add(num2)
                    if num3 not in memo:
                        if num3 > 1000 or num3 <0:
                            if num1 == goal:
                                # print('goal3',depth)
                                result = depth + 1
                                resultFlag = 1
                        else:
                            stack.append(num3)
                            memo.add(num3)
            
            if resultFlag:
                return result
            depth +=1

        return -1


if __name__ == '__main__':
    solu = Solution()
    # distance = [2,1,1,2]
    # distance = [1,2,3,4]
    # nums = ["Hello","Alaska","Dad","Peace"]
    
    nums = [1,3]
    start = 6
    goal = 4
    
    # nums = [2,4,12]
    # start = 2
    # goal = 12
    
    
    nums = [3,5,7]
    start = 0
    goal = -4
    
    nums = [2,8,16]
    start = 0
    goal = 1
    
    nums = [1]
    start = 0
    goal = 3
    
    nums = [-405,274,-344,577,-910,-936,323,-699,-952,-848,568,675,5,-209,-170,200,237,707,279,-760,248,390,531,752,62,53,-60,791,-807,-493,812,-995,-745,-528,776,437,-306,-237,-333,-845,-858,-71,-198,360,-495,-416,15,-393,-935,-117,-776,-964,127,909,-983,586,855,-563,-570,-394,717,-527,-624,441,47,446,481,297,268,764,-918,969,203,461,-937,293]
    start = 438
    goal = 927
    
    nums = [-783,696]
    start = 43
    goal = 161
    
    result = solu.minimumOperations(nums,start,goal)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)