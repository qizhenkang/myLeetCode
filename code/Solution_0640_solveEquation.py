# -*- coding: utf-8 -*-
"""
Created on 2022/08/10 09:19:07

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        """
        solveEquation _summary_

        用 re 不太合理 要逐个读入字符比较合理

        用了 30 min 4 次提交成功 没啥意思这题

        Args:
            equation (str): _description_

        Returns:
            str: _description_
        """

        left_flag = True
        num_flag = False
        sign = +1

        temp_num = 0
        bias = 0
        x = 0

        x_left = 0
        bias_left = 0

        x_right = 0
        bias_right = 0

        for s in equation:

            if s == '+' or s == '-' or s == '=':

                bias = sign * temp_num
                if left_flag:
                    bias_left += bias
                else:
                    bias_right += bias
                temp_num = 0
                if s == '+':
                    sign = +1
                elif s == '-':
                    sign = -1
                if s == '=':
                    left_flag = False
                    sign = +1
                num_flag = False
            elif s == 'x':
                if temp_num == 0 and not num_flag:
                    temp_num = 1
                bias = sign * temp_num
                if left_flag:
                    x_left += bias
                else:
                    x_right += bias
                temp_num = 0
            else:
                temp_num = temp_num*10 + int(s)
                num_flag = True

            # print(s, sign, temp_num, bias_right)

        if temp_num:
            bias_right += sign * temp_num

        if x_left == x_right:
            if bias_left == bias_right:
                result = "Infinite solutions"
            else:
                result = "No solution"
        else:
            num = int((bias_right - bias_left) / (x_left-x_right))
            result = 'x=%d' % num
        # print('%dx' % x_left, '+', bias_left, '=',
        #       '%dx' % x_right, '+', bias_right)
        # print(result)
        return result


if __name__ == '__main__':
    solu = Solution()

    result = solu.solveEquation('0x=0')

    # assert result == 'x=1'
