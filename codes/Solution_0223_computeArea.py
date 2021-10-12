# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 00:06:41 2021

@author: qizhe
"""

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
        和答案一模一样，巧妙的地方在于充分利用了max min 的作用，从而考虑了各种情况
        用时10min
        """
        Area1 = (ax2-ax1)*(ay2-ay1)
        Area2 = (bx2-bx1)*(by2-by1)
        
        xCross = max(min(ax2,bx2) - max(ax1,bx1), 0)
        yCross = max(min(ay2,by2) - max(ay1,by1), 0)
        
        
        AreaCross = xCross*yCross
        # print(Area1,Area2,AreaCross)
        
        return Area1 + Area2 - AreaCross
        
        


if __name__ == '__main__':
    solu = Solution()

    ax1 = -3
    ay1 = 0
    ax2 = 3
    ay2 = 4
    bx1 = 0
    by1 = -1
    bx2 = 9
    by2 = 2
    
    # ax1 = -2
    # ay1 = -2
    # ax2 = 2
    # ay2 = 2
    # bx1 = -2
    # by1 = -2
    # bx2 = 2
    # by2 = 2

    result = solu.computeArea(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2)

    # while result:
    #     print(result.val)
    #     result = result.next

    output_Str = 'result = ' + str(result)
    print(output_Str)