# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:43:08 2021

@author: qizhe
"""

class Solution:
    def countSegments(self, s: str) -> int:
        """
        目标: 识别上升沿（空格变非空格）
        3min结束战斗 
        用时96% 内存64%
        """
        
        result = 0
        state = 0
        for st in s:
            if st == ' ':
                state = 0
            else:
                if not state:
                    result += 1
                    state = 1
        
        return result
        
        
if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    intervals = "Hello, my name is John"
    # input_List = [[1,2,3],[4,5,6],[7,8,9]]
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.countSegments(intervals)

    output_Str = ' result = ' + str(result) 
    print(output_Str)