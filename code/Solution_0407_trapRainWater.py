# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 09:25:43 2021

@author: Zhenkang
"""
import heapq
from typing import List
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        读题：
        1、原版接雨水是一维的，要用“单调栈”
        2、这个感觉要搜索呢，单调栈还可以嘛？
        3、动态规划，有可能吗
        
        确实比较难，不太确定怎么做，看看答案吧
        答案：
        1、答案也不是一下看懂的，抄过来写一下注释吧
        2、有点懂了，就是先找最外圈，再找最外圈的最矮，最矮旁边的可以确定
        
        肯定不是特别懂，有时间要再看
        
        """
        # 小于3个就直接返回了
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    # 最外层都入堆
                    visited[i][j] = 1
                    heapq.heappush(pq, (heightMap[i][j], i * n + j))
        
        res = 0
        # 方向？
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            # 弹出，原高度和位置
            height, position = heapq.heappop(pq)
            # print('pop: \t',len(pq),height,position // n,position % n)
            for k in range(4):
                # 4个方向，其实就是把position再破译回去，再加上位置
                nx, ny = position // n + dirs[k], position % n + dirs[k + 1]
                # 得到新位置，不能走出去了，并且不能走过
                if nx >= 0 and nx < m and ny >= 0 and ny < n and visited[nx][ny] == 0:
                    # 判断是否低于 height
                    if height > heightMap[nx][ny]:
                        # 记录接水量
                        res += height - heightMap[nx][ny]
                    # 记录走过
                    visited[nx][ny] = 1    
                    # 入堆，再次记录最大值
                    heapq.heappush(pq, (max(height, heightMap[nx][ny]), nx * n + ny))
                    # print('push: \t',len(pq),max(height, heightMap[nx][ny]), nx,ny)
        return res



if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    # input_Str = str('LEETCODEISHIRING')
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    output_Str = 'result = ' + str(solu.trapRainWater(heightMap))
    print(output_Str)
