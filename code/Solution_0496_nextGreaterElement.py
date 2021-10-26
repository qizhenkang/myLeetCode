# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:12:18 2021

@author: qizhe
"""
from typing import List
# from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        读题：
        1、最简单的思路，肯定是拿到一个，然后去遍历nums2，但这样时间复杂度是 n*n
        2、能不能用空间换时间？
        3、题目中进阶的意思其实就是两个数组分别扫描一遍
        4、核心思路是“单调栈”，遍历一次，遇到大的就出栈，出栈时记录
        
        测试：
        1、10min，一次通过，性能极好
        
        答案：
        1、和答案之差一点，他用了一个数组做哈希表，有点问题呢
        
        题解里面：
        1、亲们记住，一但要求下一个更大的元素，就是用单调栈解，力扣题库相似的题目都是这个解法。
        
        """
        N1 = len(nums1)
        N2 = len(nums2)
        result = [-1] * N1
        # 扫描一次，记录下标
        nums1Dict = {nums1[i]:i for i in range(N1)}
        stack = []
        for i in range(N2):
            # print(i,stack)
            while stack and nums2[i] > stack[-1]:
                temp = stack.pop()
                if temp in nums1Dict:
                    result[nums1Dict[temp]] = nums2[i]
            stack.append(nums2[i])

        return result
    

if __name__ == '__main__':
    solu = Solution()


    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    nums1 = [2]
    nums2 = [2]

    result = solu.nextGreaterElement(nums1, nums2)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
