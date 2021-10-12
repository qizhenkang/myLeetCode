# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:35:08 2021

@author: qizhe
"""

class Solution:
    def trap(self, height) -> int:
        """
        写了半天，写了一个错误代码
        
        看了答案 这是一个好题 有很多方法
        
        可以用：
        1、DP
        2、Stack
        3、Double Pointer

        """
        
        # return self.trap_DoublePointer(height)
        return self.trap_Stack(height)
    
    
    def trap_DP(self,height) -> int:
        """
        法1：动态规划
        
        答案的动态规划思路
        总共分三次扫描：
        1、左侧填满
        2、右侧填满
        3、确定每个位置的水
        
        那么我可以改进一下：
        1、第一次扫描：从左向右，确定每个位置的左侧高度
        2、第二次扫描：从右向左，确定右侧高度的同时，直接计算得到水量
        3、求和即可
        """
        N = len(height)
        leftMax = [height[0]] * N
        rightMax = height[-1]
        # leftMax[0] = height[0]
        for i in range(1,N):
            leftMax[i] = max(leftMax[i-1],height[i])
        
        # print(leftMax)
        leftMax[-1] = 0
        for i in range(N-2,-1,-1):
            rightMax = max(rightMax,height[i])
            leftMax[i] = min(leftMax[i],rightMax) - height[i] + leftMax[i+1]
        
        return leftMax[0]
    
    def trap_Stack(self,height) -> int:
        """
        这种方法维护了一个栈，
        这个栈存储的是下标，通过一次遍历就完成了任务
        单调栈，意思是单调递减时压栈
        """
        
        result = 0
        stack = []
        
        for i in range(len(height)):
            
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                result += (i - left - 1)*(min(height[left],height[i]) - height[top])
            # print(stack)
            stack.append(i)
        
        return result
    
    def trap_DoublePointer(self,height) -> int:
        """
        法3：双指针
        
        有一种取巧的办法，只要对侧有高值，则此侧必为低值，可以直接计算
        这样只需要双指针的一次遍历
        
        """
        N = len(height)
        leftMax = 0
        rightMax = 0
        # leftMax[0] = height[0]
        left = 0
        right = N-1
        
        result = 0
        while left < right:
            leftMax = max(leftMax,height[left])
            rightMax = max(rightMax,height[right])
            if height[left] <height[right]:
                result += leftMax - height[left]
                left +=1
            else:
                result += rightMax - height[right]
                right -=1

        return result
        
    def error(self,height):
        # N = len(height)
        
        # if N < 3:
        #     return 0
        # peakFlag = 0
        # # peakVal = 0
        # peakPosi = -1
        # state = 0
        
        # waterTotal = 0
        # waterCurrent = 0
        # waterboolwidth = 0
        
        # for i in range(N):
        #     if i == 0:
        #         if height[0] > height[1]:
        #             # peakVal = height[0]
        #             # peakPosi = 0
        #             state = 1
        #             peakFlag = 1
        #         else:
        #             peakFlag = 0
                    
        #     elif i == N-1:
        #         if height[N-2] < height[N-1]:
        #             # peakVal = height[N-1]
        #             # peakPosi = N-1
        #             state = 1
        #             peakFlag = 1
        #         else:
        #             peakFlag = 0
        #     else:
        #         if height[i-1] < height[i] and height[i] > height[i+1]:
        #             # peakVal = height[i]
        #             # peakPosi = i
        #             state = 1
        #             peakFlag = 1
        #         elif state:
        #             if height[peakPosi] <= height[i]:
        #                 state = 0
        #                 peakFlag = 1
        #         else:
        #             peakFlag = 0
            
            
        #     if peakFlag:
        #         if height[peakPosi] > height[i]:
        #             waterCurrent -= (i - peakPosi - 1) * (height[peakPosi] - height[i])
        #         waterTotal += waterCurrent
        #         waterCurrent = 0
        #         peakPosi = i
        #         peakFlag = 0
        #     elif state:
        #         waterCurrent += height[peakPosi] - height[i]
        #         waterboolwidth +=1
        #     else:
        #         pass
            
        #     print(i,waterTotal)
            

        # return waterTotal
        return 0
        
        



if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    # input_List = [0,1,0,2,1,0,1,3,2,1,2,1]
    input_List = [4,2,0,3,2,5]
    # input_List = [[-10]]
    # input_int = 6

    result = solu.trap(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)