# -*- coding: utf-8 -*-
"""
Created on 2022/09/01 10:30:42

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        finalPrices 

        模拟可以，但是查询次数特别大
        单调栈是正解，意思是维护一下右侧的第一个小的

        Args:
            prices (List[int]): _description_

        Returns:
            List[int]: _description_
        """

        length = len(prices)
        result = [0 for _ in range(length)]

        stack = [0]

        for i in range(length-1, -1, -1):

            while len(stack) > 1 and stack[-1] > prices[i]:
                stack.pop()
            result[i] = prices[i] - stack[-1]
            stack.append(prices[i])

        return result


if __name__ == '__main__':
    solu = Solution()

    print(solu.finalPrices([8, 4, 6, 2, 3]))
