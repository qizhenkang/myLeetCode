# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:55:10 2021

@author: qizhe
"""
from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        """
        读题：
        1、感觉上就是一个统计数字个数
        2、直接用一个Set记录长度
        3、感觉用set坏处是空间复杂，可以写一个遍历，统计一下

        测试：
        1、一次通过，2min结束吧

        答案：
        1、竟然和答案思路一模一样

        答案：
        
        """
        numSet = set(candyType)

        return len(numSet) if len(numSet) < len(candyType)//2 else len(candyType)//2