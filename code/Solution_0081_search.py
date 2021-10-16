# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:40:32 2021

@author: qizhe
"""

class Solution:
    def search(self, nums, target: int) -> bool:
        """
        读题：
        1、好像之前做过，感觉唯一不一样的条件是，这个数组是一个可以重复的数组
        2、基本思路应该不变
        3、难点在于边界条件的处理
        
        测试：
        1、极端例子，没有通过
        
        
        不会加了，看了答案 加了一个条件结束了
        答案：
        1、
        """
        N = len(nums)
        
        left = 0
        right = N-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # print(left,mid,right)
            
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                # 这个条件是看的答案，当三者相等时无法判断，++--
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        
        return False

        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1
    nums = [0,0,1,1,1,1,2,3,3]
    # nums = [3,5,6,0,0,1,2]
    # target = 2
    nums = [1,0,1,1,1]
    target = 0
    

    result = solu.search(nums,target)

    output_Str = ' result = ' + str(result)
    print(output_Str)