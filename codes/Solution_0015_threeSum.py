import string
import math
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n_length = len(nums)
        nums.sort()  # ? 先排序
        for i in range(0, n_length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left = i + 1
            right = n_length - 1
            while True:
                if left >= right:
                    break
                sum = nums[left] + nums[right] + nums[i]

                

                if sum == 0:
                    result = result + [[nums[i], nums[left], nums[right]]]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left = left + 1
                    right = right - 1

                elif sum > 0:
                    right = right - 1  # 右指针左移，使sum减小
                else:
                    left = left + 1  # 左指针右移，使sum增加

        # result_new = []
        # for r in result:
        #     if r not in result_new:
        #         result_new = result_new + [r]

        return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('IX')
    input_List = [-15, 10, 0, -2, 14, -1, -10, -14, 10, 12, 6, -6, 10, 2, -11, -9, 2, 13, 2, -9, -14, -12, -10, -12, 13, 13, -10, -3, 2, -11, 3, -6, 6, 10, 7, 5, -13, 4, -2, 12, 1, -11, 14, -4, 6, -12, -6, -14, 8, 11, -8,
                  1, 7, -3, 5, 5, -13, 10, 9, -3, 6, -10, 6, -3, 7, -9, -13, 9, 10, 0, -1, -11, 4, -10, -8, -13, -15, 2, -12, 8, -2, -12, -14, -10, -8, 6, 2, -5, -7, -11, 7, 14, -6, -10, -12, 8, -4, -10, -5, 14, -3, 9, -12, 8, 14, -13]
    input_List = [-1, 0, 1, 2, -1, -4]
    input_int = 101

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(solu.threeSum(input_List))
    print(output_Str)
