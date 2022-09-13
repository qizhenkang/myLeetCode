# -*- coding: utf-8 -*-
"""
Created on 2022/09/13 10:51:35

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        maximumSwap _summary_

        找最大数和次大数，如果最大不是第一个

        如果最大是第一个，那就变成了一个问题，双指针

        15 mins 2 次通过 思想是对的，第二个指针应该从小开始算，测试算例没有构造好

        Args:
            num (int): _description_

        Returns:
            int: _description_
        """
        temp = num
        num_list = []
        while temp > 0:
            _num = temp % 10
            num_list.insert(0, _num)
            temp //= 10

        # pi = 0
        # pj = 0
        for i in range(len(num_list)):
            max_num = max(num_list[i:])
            if max_num > num_list[i]:
                for j in range(len(num_list)-1, i-1, -1):
                    if num_list[j] == max_num:
                        num_list[j] = num_list[i]
                        num_list[i] = max_num
                        break
                break

        result = 0
        for i in range(len(num_list)):
            result *= 10
            result += num_list[i]

        return result


if __name__ == '__main__':
    solu = Solution()

    print(solu.maximumSwap(2736))  # 7236
    print(solu.maximumSwap(9973))  # 9973
    print(solu.maximumSwap(1993))  # 1993
    print(solu.maximumSwap(12))  # 21
    print(solu.maximumSwap(1))  # 1
