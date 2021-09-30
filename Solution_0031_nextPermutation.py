# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:34:53 2021

@author: qizhe
"""

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        看了答案，思路基本一致，但答案的思路没有进行重新排序，而是利用了前面的操作。
        """
        N = len(nums)
        
        if N < 2:
            return
        
        lastUp = 0
        minmaxNum = 1e3
        exchange = 0
        # 第一次扫描，找最后一个升序
        for i in range(1,N):
            if nums[i-1] < nums[i]:
                lastUp = i
                exchange = i
                minmaxNum = nums[i]
            
            # 记录最小最大值
            if lastUp:
                if nums[i] > nums[lastUp-1]:
                    if nums[i] < minmaxNum:
                        minmaxNum = nums[i]
                        exchange = i
                # 也就是大于nums[lastUp-1] 的 一个最小的数
        
        if lastUp == 0:
            nums.sort()
            return nums
        # 交换位置 
        # 这里的理解出了一些问题，应该是找后侧更大的最小数交换位置
        # for i in range(lastUp+1,N):
        nums[lastUp-1], nums[exchange] = nums[exchange], nums[lastUp-1]
        
        # 后续重新排序
        exchangeFlag = 0
        for i in range(lastUp+1,N):
            for j in range(lastUp+1,N - i + lastUp + 1):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    exchangeFlag = 1
            if not exchangeFlag:
                break

        
        return nums
        



if __name__ == '__main__':
    solu = Solution()
    # input_List = [1,2,3,4]
    input_List = [4,3,2,1]
    input_List = [3,4,5,9,8,7,2] # [3,4,7,2,5,8,9]

    result = solu.nextPermutation(input_List)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)