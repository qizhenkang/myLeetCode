# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:27:29 2021

@author: qizhe
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Bucket = 54*[0]
        
        sortDict = dict()
        
        # 统计
        for i in s:
            if i in sortDict:
                sortDict[i] += 1
            else:
                sortDict[i] = 1
        dortlist = sorted(sortDict.items(),key=lambda item: item[1],reverse=True)
        result = ''
        for i in dortlist:
            result += ''.join(i[1] * i[0])

        return result

        
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [3,3,1,3]

    result = solu.frequencySort(input_Str)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)