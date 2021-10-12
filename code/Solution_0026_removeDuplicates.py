# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:19:50 2021

@author: qizhe
"""
# 这里和答案不太一样，对题目的理解有点问题
# 题目要求填入前面，后面不管，
# 答案用的是快慢指针


class Solution:
    def removeDuplicates(self, nums):
        Datalength = len(nums)
        if Datalength <= 1:
            return Datalength

        # 已经升序排列，只需要两个指针即可
        pointer1 = 0
        pointer2 = 1
        deletelength = 0
        while(pointer2 < Datalength - deletelength):
            if(nums[pointer1] == nums[pointer2]):
                nums.pop(pointer2)
                deletelength = deletelength +1
            else:
                pointer1 = pointer1 + 1
                pointer2 = pointer2 + 1

        return len(nums)


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('{[]{}()}')
    # input_list =
    input_List = [0, 0,2]
    input_int = 4

    result = solu.removeDuplicates(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
