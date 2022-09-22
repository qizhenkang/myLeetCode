# -*- coding: utf-8 -*-
"""
Created on 2022/09/22 18:43:05

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        canFormArray _summary_

        题意读明白了，是一个搜索

        arr 中每个整数互不相同，一下就简单了

        8 min 一次通过

        Args:
            arr (List[int]): _description_
            pieces (List[List[int]]): _description_

        Returns:
            bool: _description_
        """

        p1 = 0

        # 和答案思路基本一致
        # 答案用的是哈希表，我用的是 基于使用，稍微有点浪费时间
        piece_used = [False for _ in pieces]
        while p1 < len(arr):
            no_solution_flag = True
            for i, piece in enumerate(pieces):
                if not piece_used[i]:
                    piece_len = len(piece)
                    # print(piece, arr[p1:p1+piece_len])
                    if piece == arr[p1:p1+piece_len]:
                        # print(p1, p1+piece_len)
                        p1 += piece_len
                        no_solution_flag = False
                        piece_used[i] = True
                        break

            if no_solution_flag:
                break

        if p1 >= len(arr):
            return True

        return False


if __name__ == '__main__':

    solu = Solution()

    arr = [15, 88]
    pieces = [[88], [15]]
    print(solu.canFormArray(arr, pieces))  # true

    arr = [49, 18, 16]
    pieces = [[16, 18, 49]]
    print(solu.canFormArray(arr, pieces))  # false

    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    print(solu.canFormArray(arr, pieces))  # true
