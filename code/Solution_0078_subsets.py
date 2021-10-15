# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 22:01:07 2021

@author: qizhe
"""

class Solution:
    def subsets(self, nums):
        """
        读题：
        1、学会回溯之后，一看这种暴力遍历的题就想做啊
        2、主要的思路就是回溯，逐个的加入就是了
        3、感觉不需要回溯，只需要一个位运算就可以呢
        
        测试：
        1、一遍通过，感觉和答案应该很接近
        """
        # def dfs(nums):
        #     return
        
        
        result = []
        current = []
        for i in range(2**len(nums)):
            current = []
            cnt = 0
            while i>0:
                if i & 0b1:
                    current.append(nums[cnt])
                i >>= 1
                cnt += 1
            result.append(current)
        return result
    
if __name__ == '__main__':
    solu = Solution()
    
    word1 = "horse"
    
    word2 = 'ros'
    # arr = '/home//foo/'
    # arr = '/../'
    nums = [0]
    # input_List = 1
    # s = "ADOBECODEBANC"
    # t = "ABC"
    # s = 'bacd'
    # t = 'cd'
    

    result = solu.subsets(nums)

    output_Str = ' result = ' + str(result)
    print(output_Str)


        