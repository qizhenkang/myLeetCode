# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:38:44 2021

@author: qizhe
"""
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        读题：
        1、二分搜索是可以的，能不能回溯？
        2、既然回溯+二分搜索，那就来个栈呗，是吧
        
        测试：
        1、一次通过，性能不好，感觉原因是因为用到了BFS
        2、现在的思路是一个BFS，能不能DFS 是吧
        3、用到了记忆化搜索，也就是用到了空间
        
        答案：
        1、用二分啥的
        2、我的这个做法，训练了很多：1、二分查找 2、BFS DFS 迭代 3、 BFS DFS优劣对比
        """
        m = len(matrix)
        n = len(matrix[0])
        stack = [[0,m-1,0,n-1]]
        # x = 0
        # 记忆化搜索
        memo = set()
        while stack:
            # 回溯的迭代写法
            # print(stack)
            N = len(stack)
            for i in range(N):
                posi = stack.pop() # DFS 栈
                # posi = stack.pop(0) # BFS 队列
                if tuple(posi) in memo or posi[0] > posi[1] or posi[2] > posi[3]:
                    continue
                aimposi = [(posi[0]+posi[1])//2,(posi[2]+posi[3])//2]
                print(matrix[aimposi[0]][aimposi[1]],aimposi[0],posi)

                if matrix[aimposi[0]][aimposi[1]] > target:
                    stack.append([posi[0],aimposi[0],posi[2],posi[3]])
                    stack.append([posi[0],posi[1],posi[2],aimposi[1]])
                elif matrix[aimposi[0]][aimposi[1]] < target:
                    stack.append([aimposi[0]+1,posi[1],posi[2],posi[3]])
                    stack.append([posi[0],posi[1],aimposi[1]+1,posi[3]])
                else:
                    return True
                memo.add(tuple(posi))

        return False

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 27

    result = solu.searchMatrix(matrix,target)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)
        