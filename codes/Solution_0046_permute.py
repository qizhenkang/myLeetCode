# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:35:10 2021

@author: qizhe
"""

from typing import List


class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     def dfs(nums, size, depth, path, used, res):
    #         if depth == size:
    #             # 出问题的原因，可能是，path 在res里是引用的，所以path修改就会导致res也改了
    #             res.append(path[:])
    #             # 改动 path -> path[:]
    #             return

    #         for i in range(size):
    #             if not used[i]:
    #                 used[i] = True
    #                 path.append(nums[i])
    #                 # print(path)

    #                 dfs(nums, size, depth + 1, path, used, res)

    #                 used[i] = False
    #                 path.pop()
    #         # print(res)

    #     size = len(nums)
    #     if len(nums) == 0:
    #         return []

    #     used = [False for _ in range(size)]
    #     res = []
    #     dfs(nums, size, 0, [], used, res)
    #     return res
    

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            print('first = ',first)
            print('res = ',res)
            for i in range(first, n):
                # print(first,i)
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                print('nums 1 = ',nums)
                # 继续递归填下一个数
                backtrack(first + 1)
                
                print('nums 2 = ',nums)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
