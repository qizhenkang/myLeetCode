# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:36:31 2021

@author: qizhe
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        读题：
        1、不知道为什么，感觉这题见过，搞一个哈希表 还是双指针，向前走，然后再缩小，找到最小子串
        2、双指针好理解，一个前面一个后面，满足条件前，前指针移动，扩大序列；满足条件后后指针移动，缩到最小
        3、如何判断是否覆盖呢？感觉上应该是哈希表，也就是统计一下个数
        
        测试：
        1、一次通过，但性能较差
        
        答案：
        1、答案就是所谓的“滑动窗口”，与我的思路一致
        2、不太一样的地方，是用到了一个need字典，其余差别不大。
        3、我的性能差，就差在了总是在遍历字典
        
        """
        # if len(t) == 1:
        #     return t
        left = 0
        right = 0
        tDict = {}
        currentDict = {}
        
        for st in t:
            currentDict[st] = 0
            if st in tDict:
                tDict[st] += 1
            else:
                tDict[st] = 1
        okFlag = 0
        minLength = 1e6
        result = ''
        # 学习答案的思路，记录剩余长度，从而减少对于字典的遍历
        # nowCnt = 0
        while True:
            
            if not okFlag:
                if right >= len(s):
                    break
                if s[right] in tDict:
                    currentDict[s[right]] += 1
                    # nowCnt += 1

                matchFlag = 1
                for key,_ in tDict.items():
                    if currentDict[key] < tDict[key]:
                        matchFlag = 0
                
                if matchFlag:
                    okFlag = 1

                right += 1
            else:
                # 合法情况，尽可能缩小
                if s[left] in tDict:
                    currentDict[s[left]] -= 1
                
                matchFlag = 1
                for key,_ in tDict.items():
                    if currentDict[key] < tDict[key]:
                        matchFlag = 0
                    
                if not matchFlag:
                    if right-left < minLength:    
                        minLength = right-left
                        result = s[left:right]
                    okFlag = 0
                    
                left += 1
            # print(left,right,okFlag,currentDict)
            
        
        return result
        
        


if __name__ == '__main__':
    solu = Solution()
    
    word1 = "horse"
    
    word2 = 'ros'
    # arr = '/home//foo/'
    # arr = '/../'
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # input_List = 1
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = 'bacd'
    t = 'cd'
    

    result = solu.minWindow(s,t)

    output_Str = ' result = ' + str(result)
    print(output_Str)
