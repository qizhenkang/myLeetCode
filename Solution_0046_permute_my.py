# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:01:15 2021

@author: qizhe
"""

class Solution:
    def permute(self, nums):
        """
        回溯法的第一道题，糊里糊涂地做对了，大概的特点是
        1、本质是暴力递归，递归前后要恢复现场
        2、每次递归修改的内容是 交换顺序
        3、设置终止条件，要返回

        Parameters
        ----------
        nums : TYPE
            DESCRIPTION.

        Returns
        -------
        result : TYPE
            DESCRIPTION.

        """
        def Backtracking(nums,result,first):
            if first == len(nums) - 1:
                result.append(nums[:])
                # print(first,' ',nums)
                return
            for i in range(first,len(nums)):
                
                # print(first,i,nums)

                nums[first], nums[i] = nums[i], nums[first]
                Backtracking(nums,result,first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        result = []
        
        Backtracking(nums,result,0)

        return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)