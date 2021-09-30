# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:49:13 2021

@author: qizhe
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        # 这个自己没做出来
        核心思想，是允许一个为错，一旦错了就可以删除一个，但删除的这个不知道是左边还是右边
        这时候，就如果错了，就都试试，只有两种情况，且不允许再错了
        """
        
        def checkPalindrome(low,high):
            pl = low
            pr = high
            while pl<=pr:
                if s[pl] != s[pr]:
                    return False
                pl +=1
                pr -=1
            return True
        
        pl = 0
        pr = len(s) - 1
        
        while pl<=pr:
            if s[pl]==s[pr]:
                pl +=1
                pr -=1
            else:
                return checkPalindrome(pl+1,pr) or checkPalindrome(pl,pr-1)

                
        return True


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = ['a','ab','abc','abceexxeeecba','aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga']
    for i in input_List:

        result = solu.validPalindrome(i)

        # output_Str = 'result = ' + solu.intToRoman(input_int)
        output_Str = str(i) + ' result = ' + str(result)
        print(output_Str)