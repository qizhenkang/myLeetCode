# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:19:36 2021

@author: qizhe
"""

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        目前的想法是，0在最左边，2在最右边即可，
        所以扫描的时候，找0则放到左边，找2则放到右边，找到1则原地不动
        """
        
        N = len(nums)
        if N < 2:
            return
        
        # 正式开始，主要思路是：
        # 找到0，放到左边，并记录最右0的位置
        # 找到2，放到右边，并记录最左2的位置
        zero_posi = 0
        two_posi = N - 1
        temp = 0
        i = 0
        while(i <= two_posi):
            # print(i)
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[zero_posi]
                nums[zero_posi] = temp
                zero_posi +=1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[two_posi]
                nums[two_posi] = temp
                two_posi -=1
            else:
                i +=1
                # continue
            if zero_posi > i:
                i = zero_posi
        return nums
        
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [1,2,0]
    
    result = solu.sortColors(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)