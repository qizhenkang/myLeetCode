# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:00:41 2021

@author: qizhe
"""

class Solution:     
    def balancedStringSplit(self, s: str) -> int:
        
        result = 0
        floatpoint = 0
        
        for i in s:
            if i == 'R':
                floatpoint += 1
            elif i == 'L':
                floatpoint -= 1
            else:
                pass
            
            if floatpoint == 0:
                result += 1
        
        return result

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = ['RLRRLLRLRL','RL','RLRRRLLRLL','']
    # for i in input_List:

    result = solu.balancedStringSplit(input_List[3])

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)