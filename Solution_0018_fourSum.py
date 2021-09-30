import string
import math
from typing import List
import numpy as np


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        N = len(nums)
        # 目标数 - 保证复用
        AimNum = 4
        if N < AimNum:
            return result

        pointer = np.array([0, 1, N-2, N-1])

        # 升序排序
        nums.sort()
        for p1 in range(0, N-AimNum+1):
            for p2 in range(p1+1, N-AimNum+2):
                for p3 in range(p2+1, N-AimNum+3):
                    for p4 in range(p3+1, N-AimNum+4):
                        # 计算当前和
                        sum = nums[p1]+nums[p2]+nums[p3]+nums[p4]

                        if sum == target:
                            aimCom = [[nums[p1], nums[p2], nums[p3], nums[p4]]]
                            flag = 0
                            for re in result:
                                if aimCom[0] == re:
                                    flag = 1
                                    break
                            if flag == 0:
                                result = result + aimCom

                        if sum > target:
                            break

                            # result = list(set(result))
        return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('')
    # input_list =
    input_List = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
    input_int = 200

    result = solu.fourSum(input_List, input_int)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
