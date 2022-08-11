# -*- coding: utf-8 -*-
"""
Created on 2022/08/11 10:02:38

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def reformat(self, s: str) -> str:

        numbers = []
        alphas = []
        for i in s:
            if i.isdigit():
                numbers.append(i)
            else:
                alphas.append(i)

        numbers_len = len(numbers)
        alphas_len = len(alphas)

        if abs(numbers_len - alphas_len) > 1:
            return ""

        result = []

        if numbers_len > alphas_len:
            for i in range(alphas_len):
                result.append(numbers[i])
                result.append(alphas[i])
            result.append(numbers[-1])
        elif numbers_len < alphas_len:
            for i in range(numbers_len):
                result.append(alphas[i])
                result.append(numbers[i])
            result.append(alphas[-1])
        else:
            for i in range(alphas_len):
                result.append(numbers[i])
                result.append(alphas[i])

        return "".join(result)


if __name__ == '__main__':
    solu = Solution()

    print(solu.reformat('a0b1c2'))
    print(solu.reformat('leetcode'))
    print(solu.reformat('1229857369'))
    print(solu.reformat('covid2019'))
    print(solu.reformat('ab123'))
