# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 21:16:15 2021

@author: qizhe
"""

class Solution:
    def countQuadruplets(self, nums) -> int:
        """
        感觉就是一个所谓的四数之和为零
        不太清楚这是一种什么题型
        """
        # if len(nums) < 4:
        #     return 0
        # 先排一下序
        nums.sort()
        
        # 既然是求和，那么就先确定目标数，从大到小
        pr = len(nums) - 1
        
        pl1 = 0 
        pl2 = 1
        pl3 = 2
        # 记录满足次数
        result = 0
        
        while pl1 <= pr - 3:
            
            aimNum = nums[pl1] + nums[pl2] + nums[pl3]
            
            if aimNum < nums[pr]:
                
            elif aimNum > nums[pr]:
                
            else:
                result +=1

        return result
    

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    input_List = [1,1,1,5,3]
    # input_List = ['RLRRLLRLRL','RL','RLRRRLLRLL','']
    # input_List = TreeNode(3)
    # input_List.left = TreeNode(9)
    # input_List.right = TreeNode(20)
    # input_List.right.left = TreeNode(15)
    # input_List.right.right = TreeNode(7)
    # for i in input_List:

    result = solu.countQuadruplets(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)
    
