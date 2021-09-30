# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:24:27 2021

@author: qizhe
"""

class Solution:
    def findPeakElement(self, nums) -> int:
        """
        本质上是在找局部最大值，采用了一个近似二分查找的方式
        
        是不是就是所谓的“梯度下降”

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
        pr = len(nums) - 1
        if pr == 0:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[pr] > nums[pr-1]:
            return pr
        while pl < pr:
            
            mid = int((pl + pr)/2)
            
            if nums[mid] < nums[mid+1]:
                pl = mid + 1
                if nums[pl] > nums[pl + 1]:
                    return pl
            else:
                if nums[mid] > nums[mid-1]:
                    return mid
                pr = mid - 1
                if nums[pr] > nums[pr - 1]:
                    return pr




if __name__ == '__main__':
    solu = Solution()
    
    input_List = [1,6,5,4,3,2,1]
    
    result = solu.findPeakElement(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)