# -*- coding: utf-8 -*-
"""
Created on 2022/09/18 09:25:15

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from collections import Counter
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        largestIsland _summary_

        hard problem 学习一下 想想就麻烦的题目

        事实上就是一个纯暴力搜索
        1. 先搜索所有的岛屿，编号、并记录面积
        2. 搜索所有可能的添加方式，记录新的岛屿面积

        Args:
            grid (List[List[int]]): _description_

        Returns:
            int: _description_
        """
        n = len(grid)
        tag = [[0] * n for _ in range(n)]  # 记录未访问
        area = Counter()

        def dfs(i: int, j: int) -> None:
            # 记录岛屿
            tag[i][j] = t
            area[t] += 1

            # 向四个方向搜索
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                # 在边界内 & 为陆地 & 且未访问
                if 0 <= x < n and 0 <= y < n and grid[x][y] and tag[x][y] == 0:
                    dfs(x, y)

            return

        # 深度优先搜索
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x and tag[i][j] == 0:  # 枚举没有访问过的陆地
                    t = i * n + j + 1
                    dfs(i, j)
        # 事实上没有想象的复杂，只需要一次遍历图就可以获得现存岛屿
        # 到这里就标识出了所有的岛屿，且有编号 & 每个岛屿的大小
        ans = max(area.values(), default=0)

        # 然后找所有可能的添加位置
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:  # 枚举可以添加陆地的位置
                    new_area = 1
                    connected = {0}
                    # 向四个方向搜索
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        # 在边界内 & 非同一岛屿
                        if 0 <= x < n and 0 <= y < n and tag[x][y] not in connected:
                            # 这里有一个关键技巧
                            # 1. 其实是想算周围的所有岛之和
                            # 2. 还要防止重复记录
                            new_area += area[tag[x][y]]
                            connected.add(tag[x][y])

                    # 记录最大的面积
                    ans = max(ans, new_area)
        return ans


if __name__ == '__main__':
    pass
