# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 15:18:19 2021

@author: qizhe
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        pre = 1
        cur = 2
        for _ in range(2,n):
            cur, pre = cur + pre, cur

        return cur

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [5,1,5]
    input_Num = 5

    # for i in input_List:

    result = solu.climbStairs(input_Num)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)