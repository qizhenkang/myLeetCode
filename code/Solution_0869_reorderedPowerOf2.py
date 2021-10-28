# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 08:55:46 2021

@author: qizhe
"""
from collections import defaultdict
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        读题：
        1、感觉像是一个二分查找
        2、需要判断是否满足，以及方向
        3、思路是，首先通过数字位数判断可选的，然后顺序查找
        
        测试：
        1、一次通过，20min，性能极好双80%
        
        答案：
        1、与思路二一致，思路一是回溯，列举所有可能性
        2、我其实是比答案更近了一步，先比较了数字位数，再来统计个数
        3、答案的哈希表，直接用的是列表的自然哈希
        """
        i = 0
        nDict = defaultdict()
        num = n
        bits = 0
        while num>0:
            nDict[num%10] = nDict[num%10] + 1 if num % 10 in nDict else 1
            bits += 1
            num //= 10

        bitslist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]
        # for i in range(31):
        #     num = 2 ** i
        #     while num>0:
        #         bitslist[i] += 1
        #         num //= 10
        # print(bitslist)
        
        for i in range(31):
            # print(bits,bitslist[i])
            if bits < bitslist[i]:
                break
            elif bits == bitslist[i]:
                iDict = defaultdict()
                inum = 1 << i
                while inum > 0:
                    iDict[inum%10] = iDict[inum%10] + 1 if inum % 10 in iDict else 1
                    inum //= 10
                # print(iDict)
                if nDict == iDict:
                    return True
        return False
            

        

if __name__ == '__main__':
    solu = Solution()

    n = 4013
    result = solu.reorderedPowerOf2(n)
    # for i in result:
    #     print(i)
    
    output_Str = 'result = ' + str(result)
    print(output_Str)