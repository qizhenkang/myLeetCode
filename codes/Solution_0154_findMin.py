# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:00:47 2021

@author: qizhe
"""

class Solution:
    def findMin(self, nums) -> int:
        """
        二分查找找旋转数组的最小值，关键点是允许存在重复元素。

        Parameters
        ----------
        nums : TYPE
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        
        pl = 0
        pr = len(nums)-1

        minVal = min(nums[pl],nums[pr]) # 最大值是5000
        
        while(pl<pr - 1):
            # 找中间元素，大于还是小于
            pm = int((pl+pr)/2)
            if nums[pm] < minVal:
                minVal = nums[pm]

            if nums[pl] + nums[pr] < 2 * nums[pm]:
                pl = int((pl+pr)/2)
            elif nums[pl] + nums[pr] < 2 * nums[pm]:
                pr = int((pl+pr)/2)
            else:
                pr -= 1
                if nums[pr] < minVal:
                    minVal = nums[pr]
                
            
        return minVal
        
        
        
        
        
        


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [3,3,1,3]

    result = solu.findMin(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)