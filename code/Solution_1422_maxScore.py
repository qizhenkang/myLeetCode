# -*- coding: utf-8 -*-
"""
Created on 2022/08/14 10:37:24

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def maxScore(self, s: str) -> int:

        zero_left = 0
        one_right = 0
        for i in s:
            if i == '1':
                one_right += 1

        max_score = 0
        for i in s[:-1]:
            if i == '0':
                zero_left += 1
            else:
                one_right -= 1
            cur_score = zero_left + one_right
            max_score = max(max_score, cur_score)

        return max_score


if __name__ == '__main__':

    solu = Solution()
    print(solu.maxScore('011101'))
    print(solu.maxScore('00111'))
    print(solu.maxScore('1111'))
    print(solu.maxScore('0000'))
    print(solu.maxScore('00'))
    print(solu.maxScore('11'))
