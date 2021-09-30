import string
import math
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        h_min = 0
        h_Length = len(height)
        for i in range(h_Length):
            for j in range(i, h_Length):
                h_min = height[i] * \
                    (j - i) if height[i] < height[j] else height[j] * (j - i)

                result = h_min if h_min > result else result

        return result


if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    input_Str = str('    -42  3sd')
    input_List = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # input_num = 11223
    output_Str = 'result = ' + str(solu.maxArea(input_List))
    print(output_Str)
