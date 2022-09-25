# -*- coding: utf-8 -*-
"""
Created on 2022/09/25 15:54:25

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        rotatedDigits _summary_

        读题一遍就知道了，但还是不是很懂在考什么，是不是搜索啊。

        0-9里面只有4个数对吧。 好像有点懂了

        逐个判断数字的个数

        没想明白，看答案了

        共有两种思路：

        1. 简单模拟
        2. 数位 DP
            dfs

        Args:
            n (int): _description_

        Returns:
            int: _description_
        """
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]

        ans = 0
        for i in range(1, n + 1):
            num = [int(digit) for digit in str(i)]
            valid, diff = True, False
            for digit in num:
                if check[digit] == -1:
                    valid = False
                elif check[digit] == 1:
                    diff = True
            if valid and diff:
                ans += 1

        return ans
        # def good_num(x) -> int:
        #     result = 1
        #     if x >= 9:
        #         result = 4
        #     elif x >= 6:
        #         result = 3
        #     elif x >= 5:
        #         result = 2
        #     elif x >= 2:
        #         result = 1

        #     return result
        # cnt = 1
        # weight = 1
        # while n:
        #     digit = n % 10
        #     cnt *= good_num(digit)
        #     n //= 10
        #     weight *= 10

        # # if cnt == 1:

        # return cnt


if __name__ == '__main__':
    solu = Solution()

    print(solu.rotatedDigits(10))  # 4
