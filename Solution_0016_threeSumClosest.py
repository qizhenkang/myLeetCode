import string
import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        error_min = 10 ** 4
        n_Length = len(nums)
        nums.sort()  # todo 先排个序，可以减少比较次数
        result = 0
        Sum_now = 0

        for i in range(n_Length - 2):
            if error_min == 0:
                break

            left = i + 1
            right = n_Length - 1
            error_last = 10 ** 4
            while left < right:  # todo 循环开始
                print(str(i)+' '+str(left)+' '+str(right)+' ')

                Sum_now = nums[i] + nums[left] + nums[right]
                error = Sum_now - target

                if abs(error) < error_min:  # todo 判断误差大小 更新
                    error_min = abs(error)
                    result = Sum_now

                if abs(error_last) < abs(error) and error_last * error > 0:  # todo 如果误差大小在更新后反而变大了
                    break

                if error > 0:
                    right = right - 1
                else:
                    left = left + 1

                error_last = error

        return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('IX')
    input_List = [-55, -24, -18, -11, -7, -3, 4, 5, 6, 9, 11, 23, 33]
    input_int = 0

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(solu.threeSumClosest(input_List, input_int))
    print(output_Str)
