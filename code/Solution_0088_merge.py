# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:21:20 2021

@author: qizhe
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        读题：
        1、从后往前比较合理，从最大的开始呗，是吧
        
        测试：
        1、10min 一次通过，性能不好
        2、未改动，二次测试，性能极好
        
        答案：
        1、与答案最优思路一致
        """
        p1 = m-1
        p2 = n-1
        for p in range(m+n-1,-1,-1):
            if p1 >=0 and p2 >= 0:
                if nums1[p1] < nums2[p2]:
                    nums1[p] = nums2[p2]
                    p2 -=1
                else:
                    nums1[p] = nums1[p1]
                    p1 -=1
            else:
                nums1[p] = nums1[p1] if p1 >= 0 else nums2[p2]
                p1 -= 1
                p2 -= 1
        
        return nums1

if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]

    n = 8
    inputList = [1]
    inputList = [2, 0, 5, 6, 2, 3]
    matrix = [["0","1","0","1","0"],["1","1","0","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = []
    matrix = [["0"],['1']]
    matrix = [["1","0"]]
    # inputList = [2, 2]
    # time = 3
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    result = solu.merge(nums1,m,nums2,n)

    output_Str = ' result = ' + str(result)
    print(output_Str)
    