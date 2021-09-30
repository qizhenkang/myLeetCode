# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 22:57:37 2021

@author: qizhe
"""

class Solution:
    def generate(self, numRows: int):
        
        result = [[1]]
        
        for i in range(1,numRows):
            result.append([1]*(i+1))
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        # print(result)
        return result

        


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [1,3,5]
    input_int = 1

    result = solu.generate(input_int)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)