# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:00:40 2021

@author: qizhe
"""
from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        读题：
        1、哈希表+遍历
        
        测试：
        1、一次通过
        
        答案：
        1、用了一个行号哈希
        """
        firstWords = set('qwertyuiopQWERTYUIOP')
        secondWords = set('asdfghjklASDFGHJKL')
        thirdWords = set('zxcvbnmZXCVBNM')
        result = []
        for word in words:
            if word[0] in firstWords:
                classNum = 1
            elif word[0] in secondWords:
                classNum = 2
            else:
                classNum = 3
            OKFlag = 1
            for n in word:
                if classNum == 1 and n not in firstWords or classNum == 2 and n not in secondWords or classNum == 3 and n not in thirdWords:
                    OKFlag = 0
                    break
            if OKFlag:
                result.append(word)
        return result


if __name__ == '__main__':
    solu = Solution()
    # distance = [2,1,1,2]
    # distance = [1,2,3,4]
    nums = ["Hello","Alaska","Dad","Peace"]
    result = solu.findWords(nums)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)