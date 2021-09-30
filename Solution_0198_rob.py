# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 15:30:11 2021

@author: qizhe
"""

class Solution:
    def rob(self, nums) -> int:
        """
        动态规划入门题目

        Parameters
        ----------
        nums : TYPE
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        pre = 0
        cur = 0
        
        for i in nums:
            cur,pre = max(cur,pre + i),cur
        
        return cur
    
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [2,7,9,3]
    input_Num = 5

    # for i in input_List:

    result = solu.rob(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)