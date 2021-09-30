# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:47:51 2021

@author: qizhe
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        """
        DP问题，抽象问题为，以i结尾的最大和，然后最大值即可
        """
        maxSum = nums[0]
        isum = nums[0]

        for i in nums[1:]:
            isum = max(isum + i, i)
            maxSum = max(maxSum, isum)

        return maxSum


if __name__ == '__main__':
    solu = Solution()

    input_List = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    input_List = [0]

    result = solu.maxSubArray(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)