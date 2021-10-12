# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:38:45 2021

@author: qizhe
"""
class Solution:
    def searchInsert(self, nums, target):
        # 本质上就是二分搜索，要求时间快，那就多搞几个指针
        
        low = 0
        high = len(nums) - 1
        now = int((low+high)/2)
        
        if nums[low] >= target:
            return low
        if nums[high] < target:
            return high + 1
        
        while low < high - 1:
            now = int((low+high)/2)
            # print(now)
            if nums[now] == target:
                return now
            elif nums[now] < target:
                low = now
            else:
                high = now

        if nums[now] < target:
            now +=1

        return now
        
        

  
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [1,3,5]
    input_int = 1

    result = solu.searchInsert(input_List,input_int)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
