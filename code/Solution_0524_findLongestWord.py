# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:50:51 2021

@author: qizhe
"""

class Solution:
    def findLongestWord(self, s, dictionary):
        result = ''

        for sdict in dictionary:
            # 待定判断是否满足题目要求
            isornot = self.is_representation(s, sdict)
            if isornot:
                # 先判断长度，要最长
                relen = len(result)
                sdictlen = len(sdict)
                if relen < sdictlen:
                    result = sdict
                elif relen == sdictlen:
                    # 相等再判断字典序
                    if result > sdict:
                        result = sdict

        
        return result
                    
    def is_representation(self, s,sdict):
        ps = 0
        pd = 0
        # 双指针，判断pd是否可以被表示
        while ps < len(s) and pd < len(sdict):
            if s[ps] == sdict[pd]:
                ps+=1
                pd+=1
            else:
                # 不相等则s右移
                ps+=1
        
        if pd < len(sdict):
            return False
        # print(str([pd,ps]))
    
        return True

        
        
        
        
        

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    # input_List = [0,1,2, 3,4, 5,10,22,40,101]
    # for i in input_List:
        
    # input_int = i
    input_str = "bab"
    input_List = ["ba","ab","a","b"]

    result = solu.findLongestWord(input_str,input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)