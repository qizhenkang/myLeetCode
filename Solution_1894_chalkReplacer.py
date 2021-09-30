# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:47:31 2021

@author: qizhe
"""

class Solution:
    def chalkReplacer(self, chalk, k: int) -> int:
        
        k = k % sum(chalk)
        
        i = -1
        while k >= 0:
            i += 1
            k -= chalk[i]
        
        return i


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [5,1,5]
    input_Num = 22

    # for i in input_List:

    result = solu.chalkReplacer(input_List,input_Num)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)