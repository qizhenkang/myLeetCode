import string
import math
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        Area = 0
        pointer_l = 0  # !左指针
        pointer_r = len(height) - 1  # !右指针
        while pointer_r > pointer_l:
            
            if height[pointer_l] > height[pointer_r]:
                Area = height[pointer_r] * (pointer_r - pointer_l)  # todo 1 计算当前面积
                pointer_r = pointer_r - 1

            else:
                Area = height[pointer_l] * (pointer_r - pointer_l)  # todo 1 计算当前面积
                pointer_l = pointer_l + 1
            result = Area if Area > result else result  # todo 2 取最大值
        return result


if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    input_Str = str('    -42  3sd')
    input_List = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # input_num = 11223
    output_Str = 'result = ' + str(solu.maxArea(input_List))
    print(output_Str)
