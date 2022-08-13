# -*- coding: utf-8 -*-
"""
Created on 2022/08/13 10:00:40

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        maxChunksToSorted _summary_

        大型列表的分块排序

        感觉像是在找尖峰，这意味着需要不断地回头看和向前看

        需要知道每个点的左侧最大值和右侧最小值，如果没有重复可以简单一些


        抄了答案，不太懂

        单调栈

        Args:
            arr (List[int]): _description_

        Returns:
            int: _description_
        """
        stack = []
        for a in arr:
            if not stack or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                while stack and stack[-1] > a:
                    stack.pop()
                stack.append(mx)
        return len(stack)


if __name__ == '__main__':
    solu = Solution()

    print(solu.maxChunksToSorted([5, 4, 3, 2, 1]))  # 1
    print(solu.maxChunksToSorted([2, 1, 3, 4, 4]))  # 4
    print(solu.maxChunksToSorted([0, 0, 1, 1, 1]))  # 5
    print(solu.maxChunksToSorted([1, 0, 1, 3, 2]))  # 3
    print(solu.maxChunksToSorted([0, 2, 1, 4, 3]))  # 3
