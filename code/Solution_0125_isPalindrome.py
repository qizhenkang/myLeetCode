# -*- coding: utf-8 -*-
"""
Created on 2022/06/24 14:18:02

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lens = len(s)

        pl = 0
        pr = lens-1

        result = True
        while pl < pr:

            while pl < pr and not s[pl].isalnum():
                pl += 1

            while pl < pr and not s[pr].isalnum():
                pr -= 1
            
            # print(pl,pr)
            # print(s[pl], s[pr])
            if s[pl].lower() == s[pr].lower():
                pl += 1
                pr -= 1
            else:
                result = False
                break
        return result


if __name__ == '__main__':

    solu = Solution()

    ss = ['A man, a plan, a canal: Panama',
          "race a car",
          'r',
          '',
          'rr',
          'ra',
          '.',
          ".,"]
    for s in ss:
        re = solu.isPalindrome(s)
        print(re)
