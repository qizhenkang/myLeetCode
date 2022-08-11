# -*- coding: utf-8 -*-
"""
Created on 2022/08/11 19:12:39

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        canCompleteCircuit _summary_

        读题理解了，但没明白在考什么

        感觉有点像搜索，需要记忆化搜索


        好像在某处断掉之后，就不用再回头了，回头必然是不行的

        20 min 一次成功

        Args:
            gas (List[int]): _description_
            cost (List[int]): _description_

        Returns:
            int: _description_
        """

        n = len(gas)
        start = 0
        while start < n:
            if gas[start] >= cost[start]:
                # print(start)
                start = start
                aim_point = start
                oil = 0
                for now in range(start, start+n):
                    now %= n
                    # print(now, oil)
                    oil += gas[now] - cost[now]
                    if oil < 0:
                        if now > start:
                            start = now
                        else:
                            start = n
                        break
                else:
                    # print('return %d' % start)
                    return start
            start += 1

        return -1


if __name__ == '__main__':
    solu = Solution()
    assert -1 == solu.canCompleteCircuit([2, 3, 4], [3, 4, 3])

    assert 3 == solu.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])

    print(solu.canCompleteCircuit([1, 6], [2, 5]))
