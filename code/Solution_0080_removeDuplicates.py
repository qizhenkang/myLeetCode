# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:21:46 2021

@author: qizhe
"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        读题：
        1、感觉不难，有两个要求，一个是记录长度，一个是要移动合适的位置
        2、双指针，第一个指针向下读取，后面指针负责确定当前位置，以及最终长度
        
        测试：
        1、一次通过，性能不错
        
        答案：
        可以更快，但感觉意义不大了
        
        """
        
        i = 1
        newi = 1
        doubleFlag = 1
        while i < len(nums):
            
            if nums[i-1] == nums[i]:
                doubleFlag += 1
            else:
                doubleFlag = 1
            
            # print(i,newi,doubleFlag)
            nums[newi] = nums[i]
            if doubleFlag < 3:
                newi += 1
            i += 1
                
        
        return newi
        
        
        
        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1
    nums = [0,0,1,1,1,1,2,3,3]
    nums = [1,1,1,2,2,3]

    result = solu.removeDuplicates(nums)

    output_Str = ' result = ' + str(result)
    print(output_Str)