# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:33:29 2021

@author: Zhenkang
"""
from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        N = len(secret)
        bulls = 0
        cows = 0
        numdict = defaultdict(int)
        for i in range(N):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                numdict[secret[i]] += 1
        
        for i in range(N):
            if secret[i] != guess[i] and guess[i] in numdict and numdict[guess[i]] > 0:
                numdict[guess[i]] -= 1
                cows += 1
        
        return str(bulls) + 'A' + str(cows) +'B'
        

if __name__ == '__main__':
    solu = Solution()
    arr = [1,3,5,7,8]
    
    output_Str = 'result = ' + str(solu.getHint('0','0'))
    print(output_Str)