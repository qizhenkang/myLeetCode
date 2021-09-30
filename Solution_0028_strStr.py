# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:16:18 2021

@author: qizhe
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 整体思路为双指针，一遍扫描就可以了，时间复杂度为O(n)
        
        N = len(needle)
        # 空字符返回零
        if N == 0:
            return 0
        result = -1
        pointer = 0

        for item in haystack:
            if item == needle[0]:
                if haystack[pointer:pointer+N] == needle:
                    result = pointer
                    break
            pointer += 1
        
        return result
    
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [0, 0,2]
    input_int = 4

    result = solu.strStr(input_Str,'')

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
