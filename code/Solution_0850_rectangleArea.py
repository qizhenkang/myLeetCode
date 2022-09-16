# -*- coding: utf-8 -*-
"""
Created on 2022/09/16 16:14:51

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        rectangleArea _summary_

        直接不会

        Args:
            rectangles (List[List[int]]): _description_

        Returns:
            int: _description_
        """

        result = 0

        return result % (10**9 + 7)


if __name__ == '__main__':

    solu = Solution()
    print(solu.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))  # 6

    print(solu.rectangleArea([[0, 0, 1000000000, 1000000000]]))  # 49
