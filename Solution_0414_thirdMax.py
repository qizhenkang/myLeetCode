# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:52:18 2021

@author: qizhe
"""

class Solution:
    def thirdMax(self, nums) -> int:
        """
        主要的思路：
        1、冒泡排序，第三大即可
        2、维护一个前三大的数组即可
        本文选择第二种
        """
        # 维护数组，最大在最后，第三大为top3Max[0]
        top3Max = [-2**31-1] * 3
        top3Cnt = 0
        for n in nums:
            # print('Start',n,top3Max)
            if n > top3Max[0]:
                if n > top3Max[1]:
                    if n > top3Max[2]:
                        top3Max[0] = top3Max[1]
                        top3Max[1] = top3Max[2]
                        top3Max[2] = n
                        top3Cnt += 1
                    elif n < top3Max[2]:
                        top3Max[0] = top3Max[1]
                        top3Max[1] = n
                        top3Cnt += 1
                elif n < top3Max[1]:
                    top3Max[0] = n
                    top3Cnt += 1
            # print('End',n,top3Max,top3Cnt)
    
        return top3Max[0] if top3Cnt >=3 else top3Max[2]
        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    input_List = [1,2,-2147483648]
    # input_List = [[1,2,3],[4,5,6],[7,8,9]]
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.thirdMax(input_List)

    output_Str = ' result = ' + str(result) 
    print(output_Str)