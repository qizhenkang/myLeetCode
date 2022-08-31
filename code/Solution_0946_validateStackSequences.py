# -*- coding: utf-8 -*-
"""
Created on 2022/08/31 11:48:31

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        validateStackSequences _summary_

        流程上稍微有点错误 下午再来弄

        下午来加了3行代码就好了

        现在是抄了答案代码，简单多了

        每次都入栈，然后每次都判断栈顶与 popped

        Args:
            pushed (List[int]): _description_
            popped (List[int]): _description_

        Returns:
            bool: _description_
        """

        stack, j = [], 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return len(stack) == 0


if __name__ == '__main__':
    solu = Solution()

    print(solu.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))  # True

    print(solu.validateStackSequences(
        [1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))  # False

    print(solu.validateStackSequences([2, 1, 0], [1, 2, 0]))  # True
