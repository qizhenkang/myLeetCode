# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:30:25 2021

@author: qizhe
"""

class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        读题：
        1、第一反应，哈希表统计次数
        
        """
        result = []
        numDict1 = {}
        numDict2 = {}
        for n in nums1:
            if n not in numDict1:
                numDict1[n] = 1
    
        for n in nums2:
            if n not in numDict2:
                numDict2[n] = 1
            if n in numDict1 and n not in result:
                result.append(n)

        for n in nums3:
            if (n in numDict1 or n in numDict2) and n not in result:
                result.append(n)
        
        return result
        


if __name__ == '__main__':
    solu = Solution()

    # m = 3
    nums1 = [1,1,3,2]
    nums2 = [2,3]
    nums3 = [3]
    nums1 = [3,1]
    nums2 = [2,3]
    nums3 = [1,2]
    nums1 = [1,2,2]
    nums2 = [4,3,3]
    nums3 = [5]
    result = solu.twoOutOfThree(nums1, nums2, nums3)
    # output_Str = ' result = '
    # print(' result = ',end=' ')
    # while result:
    #     print(result.val,end=' ')
    #     result = result.next


    output_Str = ' result = ' + str(result) 
    print(output_Str)