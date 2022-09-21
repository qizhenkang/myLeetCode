# -*- coding: utf-8 -*-
"""
Created on 2022/09/21 19:06:38

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        """
        kSimilarity _summary_

        困难题，看了一下没仔细做，是元素换位的问题

        学习一下思想


        典型的广度优先搜索，因为是要找最短次数，找到一个就算数

        理解了 60%

        Args:
            s1 (str): _description_
            s2 (str): _description_

        Returns:
            int: _description_
        """
        step, n = 0, len(s1)

        # 记录变量
        q, vis = [(s1, 0)], {s1}

        def swap_str(s: str, i: int, j: int) -> str:
            t = list(s)
            t[i], t[j] = t[j], t[i]
            result = ''.join(t)
            return result

        max_steps = 50
        # 死循环
        while step < max_steps:
            tmp = q
            q = []
            print(tmp)
            # q 中记录的是，上一次的 s 和 上一次的 i
            # 这里体现的是广度优先搜索的思想
            # 把上次所有的可能都试一下
            for s, i in tmp:

                # 如果发现相等，就结束了
                if s == s2:
                    return step

                # 找第一个不相等的字符 s[i] != s2[i]
                while i < n and s[i] == s2[i]:
                    i += 1

                # 从不相等的下一个字符开始，也就是计算
                # 需要注意的是，这里只扫描了一遍
                for j in range(i + 1, n):

                    # 这句话等效于 s[j] == s2[i] and s2[i] != s2[j]
                    # 意思是把 s[i+1:] 中的元素 换到 i 位置，使之满足 s[i] == s2[i]
                    # 需要注意的是，s[j] == s2[j] 时，不需要移动
                    if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换

                        # 交换 s[i] s[j]
                        t = swap_str(s, i, j)
                        print(s, t)

                        # 看是否记录，记忆化
                        if t not in vis:
                            vis.add(t)
                            q.append((t, i + 1))

            # 步数
            step += 1

        return -1


if __name__ == '__main__':

    solu = Solution()
    s1 = "ab"
    s2 = "ba"

    print(solu.kSimilarity(s1, s2))  # 1

    s1 = "abc"
    s2 = "bca"
    print(solu.kSimilarity(s1, s2))  # 2

    s1 = "aabcccd"
    s2 = "bcccaad"
    print(solu.kSimilarity(s1, s2))  # 2
