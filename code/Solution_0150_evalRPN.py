# -*- coding: utf-8 -*-
"""
Created on 2022/08/12 14:16:37

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        evalRPN _summary_

        读题感觉挺简单的，就是一个栈的思想

        10 min 一次通过

        Args:
            tokens (List[str]): _description_

        Returns:
            int: _description_
        """

        stack = []

        op_to_binary_fn = {
            "+": lambda x, y: int(x + y),
            "-": lambda x, y: int(x - y),
            "*": lambda x, y: int(x * y),
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        for i in tokens:
            if i in op_to_binary_fn:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                num = op_to_binary_fn[i](num1, num2)
                stack.append(str(num))
                # print(num)
            else:
                stack.append(i)

        return int(stack[-1])


if __name__ == '__main__':
    solu = Solution()

    print(solu.evalRPN(["2", "1", "+", "3", "*"]))
    print(solu.evalRPN(["4", "13", "5", "/", "+"]))
    print(solu.evalRPN([
        "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
