# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:20:05 2021

@author: qizhe
"""
from collections import defaultdict
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        读题
        1、这题本身不难，建个字典统计一下就是了
        2、进阶里面让空间复杂O1
        3、其实，最多只需要返回2个数，最终需要存2个，但过程中需要想办法
        4、没想出特别好的办法，是不是可以重复利用空间
        5、排序一下好像挺好，但排序好像就超了
        
        答案：
        1、第一种方案是我的
        2、第二进阶版，没接触过想不到，是所谓的“摩尔投票法”
        3、本质上是，对拼消耗
        """
        ans = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0

        for num in nums:
            # 如果该元素为第一个元素，则计数加1
            if vote1 > 0 and num == element1:
                vote1 += 1
            # 如果该元素为第二个元素，则计数加1
            elif vote2 > 0 and num == element2:
                vote2 += 1
            # 选择第一个元素
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            # 选择第二个元素
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            # 如果三个元素均不相同，则相互抵消1次
            else:
                vote1 -= 1
                vote2 -= 1
        
        # 这里就是统计一下 剩下的这两个 element1 和 element2 在数组中有多少个
        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == element1:
                cnt1 += 1
            if vote2 > 0 and num == element2:
                cnt2 += 1  
        
        # 检测元素出现的次数是否满足要求
        if vote1 > 0 and cnt1 > len(nums) // 3:
            ans.append(element1)
        if vote2 > 0 and cnt2 > len(nums) // 3:
            ans.append(element2)

        return ans

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
    s1 = "great"
    s2 = "rgeat"
    s1 = "abcde"
    s2 = "caebd"
    nums = [1]
    result = solu.majorityElement(nums)

    output_Str = ' result = ' + str(result)
    print(output_Str)