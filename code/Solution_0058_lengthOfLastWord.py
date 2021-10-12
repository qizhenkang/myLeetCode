# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:31:57 2021

@author: qizhe
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        pointer = len(s) - 1
        wordCnt = 0
        while pointer >= 0:
            if not wordCnt:
                if s[pointer] != ' ':
                    wordCnt = 1
            else:
                if s[pointer] == ' ':
                    break
                wordCnt += 1
            pointer -= 1
        
        return wordCnt
        
        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = ' '
    result = solu.lengthOfLastWord(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)