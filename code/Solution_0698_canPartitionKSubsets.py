# -*- coding: utf-8 -*-
"""
Created on 2022/09/20 16:26:37

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        canPartitionKSubsets _summary_

        这是一个搜索问题，子集个数已知，为k

        事实上，子集和也已知，为sum(nums)/k

        然后就是深度优先的记忆化搜索了应该

        第1次提交 30 min 超时了


        一直在失败，有空再看看吧

        Args:
            nums (List[int]): _description_
            k (int): _description_

        Returns:
            bool: _description_
        """
        all = sum(nums)
        if all % k:
            return False
        per = all // k
        nums.sort()  # 方便下面剪枝
        if nums[-1] > per:
            return False
        n = len(nums)

        # @cache
        # 这里不 cache 会超时
        # cache 会报错 可能是 python 版本的问题
        def dfs(s, p):
            if s == 0:
                return True
            for i in range(n):
                if nums[i] + p > per:
                    break
                # p + nums[i] 等于 per 时置为 0
                if s >> i & 1 and dfs(s ^ (1 << i), (p + nums[i]) % per):
                    return True
            return False
        return dfs((1 << n) - 1, 0)

        # sum_nums = sum(nums)
        # if sum_nums % k != 0:
        #     return False

        # aim_sum = sum_nums // k

        # nums_len = len(nums)
        # nums_used = [False for _ in range(nums_len)]
        # current_set = []
        # sets_log = []

        # memo = []

        # def show_unused(nums_used):
        #     result = []
        #     for i, used in enumerate(nums_used):
        #         if not used:
        #             result.append(nums[i])
        #     return result

        # def dfs(sum_current, sets_num):
        #     if all(nums_used):
        #         if sets_num == k and sum_current == 0:
        #             return True
        #         else:
        #             # print('最终超过')
        #             # print(sets_num, sum_current)
        #             return False

        #     end_flag = False
        #     while True:
        #         end_flag = True
        #         print('unused', show_unused(nums_used))
        #         # if sum(show_unused(nums_used)) + :

        #         if sets_log in memo:
        #             return False

        #         for j in range(len(nums)):
        #             result = False
        #             if nums_used[j] is False:
        #                 next_sum = nums[j] + sum_current
        #                 nums_used[j] = True
        #                 if next_sum < aim_sum:
        #                     current_set.append(nums[j])
        #                     result = dfs(next_sum, sets_num)
        #                     if current_set:
        #                         current_set.pop(-1)
        #                     # end_flag = False
        #                 elif next_sum == aim_sum:
        #                     current_set.append(nums[j])
        #                     sets_log.append(current_set.copy())
        #                     current_set.clear()
        #                     print('sets_log', sets_log)
        #                     result = dfs(0, sets_num+1)

        #                     sets_log.pop(-1)
        #                     # current_set.pop(-1)
        #                     end_flag = False
        #                 nums_used[j] = False

        #             if result is True:
        #                 return True
        #         if end_flag:
        #             break

        #     memo.append(sets_log)
        #     print(memo)
        #     print('遍历超过')
        #     return False

        # return dfs(0, 0)


if __name__ == '__main__':

    solu = Solution()
    print(solu.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))  # True
    print(solu.canPartitionKSubsets([1, 2, 3, 4], 3))  # false
    print(solu.canPartitionKSubsets([1, 2, 3, 4], 4))  # false
    print(solu.canPartitionKSubsets([1, 1, 1, 1, 2, 2, 2, 2], 4))  # true
