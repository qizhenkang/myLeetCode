# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:10:18 2021

@author: qizhe
"""

class Solution:
    def canJump(self, nums) -> bool:
        """
        读题：
        1、这个题和之前一个题很像，那个是计算最小跳跃次数吧？这个题是判断是否能达到最后一个
        2、那个题，贪婪算法就可以完成了，意思是每次都找最好的那一步就可以了。
        3、这个题应该也可以这样做，看他最后停在哪里了
        4、又看了一下题目，他给的nums长度最长是3e4，好像有点不太靠谱
        5、想到，必然是存在零，否则怎么可能跳不过去呢？
        6、0前面的数足够小应该就跳不过去了，所以就是找零，然后判断。
        
        测试：
        1、遇到了一个bug，从N-2开始计才对，nums[N-1]==？没有意义
        2、用时击败99%，内存消耗击败31%
        
        答案：
        维护了一个最长距离，也挺简单
        
        首次通过用时：10min
        """
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == 0:
                canFlag = 0
                for j in range(i-1,-1,-1):
                    # print(i,j,dist)
                    if nums[j] > i-j:
                        canFlag = 1
                        break
                if not canFlag:
                    return False
        return True

if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    input_List = [1,0]
    # input_List = [[1,2,3],[4,5,6],[7,8,9]]
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.canJump(input_List)

    output_Str = ' result = ' + str(result) 
    print(output_Str)