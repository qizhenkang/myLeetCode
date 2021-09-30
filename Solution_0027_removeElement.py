# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:19:50 2021

@author: qizhe
"""


class Solution:
    def removeElement(self, nums, val):
        pfast = 0
        valCount = 0
        while(pfast < len(nums)-valCount):
            if(nums[pfast] == val):
                nums.pop(pfast)
            else:
                pfast = pfast + 1

        return len(nums)


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('{[]{}()}')
    # input_list =
    input_List = [3,2,2,3]
    input_int = 3

    result = solu.removeElement(input_List, input_int)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
