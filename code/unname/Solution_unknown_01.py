# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 10:32:29 2021

@author: Zhenkang
"""

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # 双指针
        result = 0
        vowelDict = {'a':0,
                    'e':0,
                    'i':0,
                    'o':0,
                    'u':0}
        
        newNum = 0 
        left = 0
        state = 0
        N = len(word)
        i = 0
        while left < N:
            print(left,i)
            if state == 0:
                if i<N and word[i] in vowelDict:
                    vowelDict[word[i]] += 1
                    newNum += 1
                    i += 1
                else:
                    newNum = 0
                    i += 1
                    left = i
                    vowelDict = {'a':0,
                                'e':0,
                                'i':0,
                                'o':0,
                                'u':0}
                
            else:
                if i<N and word[i] in vowelDict:
                    vowelDict[word[i]] += 1
                    newNum += 1
                    i += 1
                else:
                    left += 1
                    i = left
                    vowelDict = {'a':0,
                                'e':0,
                                'i':0,
                                'o':0,
                                'u':0}
                    vowelDict[word[left]] += 1
                    state = 0
                    

                    
                
            # 判断是否为
            if newNum >= 5:
                OKFlag = 1
                for key,val in vowelDict.items():
                    if val == 0:
                        OKFlag = 0
                        break
                
                if OKFlag:
                    # print(word[left:i])
                    result += 1
                    state = 1
                
        return result
    

if __name__ == '__main__':
    solu = Solution()
    arr = [1,3,5,7,8]
    difference = 1
    nums = [9,6,4,2,3,5,7,0,1]
    nums = [1]
    # nums = [2,7,4,5,9,0,6,8,3]
    nums = 'aeiouu'
    # difference = 1
    output_Str = 'result = ' + str(solu.countVowelSubstrings(nums))
    print(output_Str)