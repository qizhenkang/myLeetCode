# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:09:42 2021

@author: qizhe
"""

class Solution:
    def search(self, nums, target: int) -> int:
        """
        感觉这个题在哪做过，二分查找吧，左右指针
        和答案写的基本一致
        需要注意起始/终止条件，也就是所谓的“边界条件”
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            
            mid = (left + right) // 2
            print(left,mid,right)
            if nums[mid] == target:
                return mid
            
            if nums[mid] <= nums[right]:
                # mid在右半段
                
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # mid在左半段
                
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

        
if __name__ == '__main__':
    solu = Solution()
    # input_List = [1,2,3,4]
    input_List = [4,3,2,1]
    input_List = [4,5,6,7,0,1,2]
    input_aim = 2
    result = solu.search(input_List,input_aim)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)