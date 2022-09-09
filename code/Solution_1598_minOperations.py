# -*- coding: utf-8 -*-
"""
Created on 2022/09/09 21:13:09

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        minOperations _summary_

        感觉就是统计一下深度

        毫无意思的一道题，1 次通过，7 min， 0 bug
        Args:
            logs (List[str]): _description_

        Returns:
            int: _description_
        """

        depth = 0
        for log in logs:
            if log == '../':
                depth = depth-1 if depth > 0 else 0
            elif log == './':
                pass
            else:
                depth += 1

        return depth


if __name__ == '__main__':
    solu = Solution()

    print(solu.minOperations(["d1/", "d2/", "../", "d21/", "./"]))  # 2
    print(solu.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))  # 3
    print(solu.minOperations(["d1/", "../", "../", "../"]))  # 0
