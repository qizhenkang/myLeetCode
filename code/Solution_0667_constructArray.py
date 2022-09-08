# -*- coding: utf-8 -*-
"""
Created on 2022/09/08 09:26:30

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        constructArray _summary_

        读题有点复杂，n 代表 1-n 这些数字

        k 代表 相邻相差的数字，只能是 k 个

        感觉需要一个贪心算法，每次找一个所需要的差别就可以了，+ or - 

        当有一个 +k 时 就要有一个 -k

        分析不出来，提交失败了。抄答案

        发现答案和我想的一样，都是把大于1的差值只用一次，感觉几乎差一点就做出来了

        双指针有点意思。

        重写了一遍，成功了。

        Args:
            n (int): _description_
            k (int): _description_

        Returns:
            List[int]: _description_
        """

        result = [i for i in range(1, n-k)]  # 构造自增序列
        pl = n-k  # 双指针，i 从 n-k 开始；j 从 n 开始
        pr = n
        while pl <= pr:
            result.append(pl)
            if pl < pr:
                result.append(pr)
            pl += 1
            pr -= 1

        return result

        # answer = list(range(1, n - k))  # 构造一个 从 1 到 n-k-1 的 自增序列
        # i, j = n - k, n  # 双指针，i 从 n-k 开始；j 从 n 开始
        # while i <= j:  # 相遇即停止
        #     answer.append(i)
        #     if i != j:
        #         answer.append(j)
        #     i, j = i + 1, j - 1  # 指针同时向内收紧
        # return answer

        # k_cnt = 0
        # result = [1 for _ in range(n)]
        # for i in range(1, n):
        #     sign = (-1)**(i+1)
        #     delta = k-k_cnt
        #     if delta > 0:
        #         new_val = result[i-1] + delta * sign
        #         if new_val <= 0 or new_val > n or new_val < i:
        #             new_val = result[i-1] - delta * sign
        #     else:
        #         new_val = i+1
        #     result[i] = new_val
        #     k_cnt += 1

        # return result


if __name__ == '__main__':
    solu = Solution()

    print(solu.constructArray(4, 1))  # [1,2,3]
    print(solu.constructArray(3, 2))  # [1,3,2]
    print(solu.constructArray(6, 3))  # [1,3,2]
