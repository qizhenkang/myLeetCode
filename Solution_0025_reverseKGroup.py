# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:25:45 2021

@author: qizhe
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        心里想了一下，总共分三步：
        1、先向前走k步，保证存在k个，才进行翻转
        2、逐个进行翻转，并处理边界
        """
        headhead = ListNode(-1,head)
        pointerK = headhead
        pointerHead = headhead
        # 1 向前走k步
        while True:
            stack = []
            for _ in range(k):
                pointerK = pointerK.next
                if not pointerK:
                    # print('break return')
                    return headhead.next
                stack.append(pointerK)
            pointerKnext = pointerK.next
            # 2 开始翻转
            stack.pop()
            pointerHead.next = pointerK
            for _ in range(k-1):
                temp = stack.pop()
                pointerK.next = temp
                pointerK = temp
            pointerK.next = pointerKnext
            pointerHead = pointerK
        
        return headhead.next
    
        
if __name__ == '__main__':
    solu = Solution()
    # input_List = [4,5,6,7,0,1,2]
    # input_aim = 0
    # n5 = ListNode(5)
    # n4 = ListNode(4,n5)
    # n3 = ListNode(3,n4)
    # n2 = ListNode(2,n3)
    n1 = ListNode(1)

    # result = solu.swapPairs(n1)
    result = solu.reverseKGroup(n1,1)
    
    print('result = ',end ='')
    while result:
        print(result.val, end=" ")
        result = result.next
    # output_Str = 'result = ' + str(result)
    # print(output_Str)

