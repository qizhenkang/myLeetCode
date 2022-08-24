# -*- coding: utf-8 -*-
"""
Created on 2022/08/23 10:28:29

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        """
        movesToChessboard _summary_

        不要把他想成数学题，而应该想成一个暴力搜索的题目

        交换成本很高，他不是一个换一个 而是一行换一行，导致困难

        太复杂了，复制粘贴了答案

        Args:
            board (List[List[int]]): _description_

        Returns:
            int: _description_
        """
        n = len(board)
        # 棋盘的第一行与第一列
        rowMask = colMask = 0
        for i in range(n):
            rowMask |= board[0][i] << i
            colMask |= board[i][0] << i
        reverseRowMask = ((1 << n) - 1) ^ rowMask
        reverseColMask = ((1 << n) - 1) ^ colMask
        rowCnt = colCnt = 0
        for i in range(n):
            currRowMask = currColMask = 0
            for j in range(n):
                currRowMask |= board[i][j] << j
                currColMask |= board[j][i] << j
            # 检测每一行和每一列的状态是否合法
            if currRowMask != rowMask and currRowMask != reverseRowMask or \
               currColMask != colMask and currColMask != reverseColMask:
                return -1
            rowCnt += currRowMask == rowMask  # 记录与第一行相同的行数
            colCnt += currColMask == colMask  # 记录与第一列相同的列数

        def getMoves(mask: int, count: int) -> int:

            # bin(128).count('1')
            ones = mask.bit_count()
            if n & 1:
                # 如果 n 为奇数，则每一行中 1 与 0 的数目相差为 1，且满足相邻行交替
                if abs(n - 2 * ones) != 1 or abs(n - 2 * count) != 1:
                    return -1
                if ones == n // 2:
                    # 偶数位变为 1 的最小交换次数
                    return n // 2 - (mask & 0xAAAAAAAA).bit_count()
                else:
                    # 奇数位变为 1 的最小交换次数
                    return (n + 1) // 2 - (mask & 0x55555555).bit_count()
            else:
                # 如果 n 为偶数，则每一行中 1 与 0 的数目相等，且满足相邻行交替
                if ones != n // 2 or count != n // 2:
                    return -1
                # 偶数位变为 1 的最小交换次数
                count0 = n // 2 - (mask & 0xAAAAAAAA).bit_count()
                # 奇数位变为 1 的最小交换次数
                count1 = n // 2 - (mask & 0x55555555).bit_count()
                return min(count0, count1)

        rowMoves = getMoves(rowMask, rowCnt)
        colMoves = getMoves(colMask, colCnt)
        return -1 if rowMoves == -1 or colMoves == -1 else rowMoves + colMoves


if __name__ == '__main__':
    solu = Solution()

    board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
    print(solu.movesToChessboard(board))

    board = [[0, 1], [1, 0]]
    print(solu.movesToChessboard(board))

    board = [[1, 0], [1, 0]]
    print(solu.movesToChessboard(board))
