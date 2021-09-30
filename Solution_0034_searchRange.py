# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 15:58:46 2021

@author: qizhe
"""

class Solution:
    def searchRange(self, nums, target: int):
        """
        nums 是一个非递减数组，找开始和结束，那其实是先找一个，然后再找开头和结尾
        """
        N = len(nums)
        if N == 0:
            return [-1,-1]
        elif N == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        left = 0
        right = N - 1
        aimposi = -1
        # 找target
        while left <=right:
            mid = (left + right) // 2
            print(left,mid,right)
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                aimposi = mid
                break
        
        if aimposi == -1:
            return [-1,-1]
        
        # 找开头和结尾
        # result = [aimposi,aimposi]
        p1 = aimposi
        p2 = aimposi
        while p1>=0:
            if nums[p1] != target:
                break
            p1 -= 1
        p1 += 1
        while p2 < N:
            if nums[p2] != target:
                break
            p2 += 1
        p2 -= 1

        return [p1,p2]

        
if __name__ == '__main__':
    solu = Solution()
    input_List = [2]
    # input_List = [4,3,2,1]
    # input_List = [4,5,6,7,0,1,2]
    input_aim = 2
    result = solu.searchRange(input_List,input_aim)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)