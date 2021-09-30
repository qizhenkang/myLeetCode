import string
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = 0.0
        nums = nums1 + nums2
        nums.sort()
        Length = len(nums)
        if (Length % 2 == 0):  # * 是偶数的话
            result = (nums[int(Length / 2 - 1)] + nums[int(Length / 2)])/2
        else:
            result = nums[int((Length + 1) / 2 - 1)]

        return result


if __name__ == '__main__':
    solu = Solution()
    num1 = [1, 2, 3]
    num2 = [2, 3, 4]
    # result_Str = str('dvdf')
    output_Str = 'result = ' + str(solu.findMedianSortedArrays(num1, num2))
    print(output_Str)
