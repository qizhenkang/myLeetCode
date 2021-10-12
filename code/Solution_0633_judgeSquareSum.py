# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:25:15 2021

@author: qizhe
"""
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        pl = 0
        pr = int(math.sqrt(c))

        while pl <= pr:
            crt_value = pl**2 + pr**2
            if crt_value == c:
                return True
            elif crt_value < c:
                pl += 1
            else:
                pr -= 1

        return False


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [0,1,2, 3,4, 5,10,22,40,101]
    for i in input_List:
        
        input_int = i

        result = solu.judgeSquareSum(input_int)

        # output_Str = 'result = ' + solu.intToRoman(input_int)
        output_Str = str(i) + ' result = ' + str(result)
        print(output_Str)