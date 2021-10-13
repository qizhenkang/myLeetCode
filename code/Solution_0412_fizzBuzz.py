# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:29:11 2021

@author: qizhe
"""

class Solution:
    def fizzBuzz(self, n: int) :
        result = []
        for i in range(1,n+1):
            if i % 15 == 0:
                result.append('FizzBuzz')
            elif i%3 == 0:
                result.append('Fizz')
            elif i %5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result
