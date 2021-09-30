# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 23:06:53 2021

@author: qizhe
"""


class Solution:
    def getRow(self, rowIndex: int):
        
        result = [1] * (rowIndex+1)
        
        for i in range(1,rowIndex+1):
            # result.append(1)
            for j in range(i-1,0,-1):
                # 这个倒序的思路是一个很神的思路，我给想出来了，和答案一致
                result[j] += result[j-1] 
                # if j > i/2:
                #     result[j] += result[j-1] 
                # elif j == i/2:
                #     result[j] = 2 * result[j]
                # else:
                #     result[j] = result[i-j]
            
            # print(result)
                    
        # print(result)
        return result

        


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [1,3,5]
    input_int = 6

    result = solu.getRow(input_int)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)