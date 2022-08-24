# -*- coding: utf-8 -*-
"""
Created on 2022/08/24 10:26:50

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


from collections import defaultdict
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        canBeEqual _summary_

        既然能翻转，是不是，只需要判断元素呢 对吧

        提交错了一次 发现需要统计个数

        hash表 7 min 2次提交成功

        Args:
            target (List[int]): _description_
            arr (List[int]): _description_

        Returns:
            bool: _description_
        """
        hash_dict = defaultdict(lambda: 0)
        for i in target:
            hash_dict[i] += 1

        for i in arr:
            hash_dict[i] -= 1

        for val in hash_dict.values():
            if val != 0:
                return False

        return True


if __name__ == '__main__':

    solu = Solution()

    print(solu.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
    print(solu.canBeEqual([7], [7]))
    print(solu.canBeEqual([3, 7, 9], [3, 7, 11]))
