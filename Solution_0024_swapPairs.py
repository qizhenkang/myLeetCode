# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:18:07 2021

@author: qizhe
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        考虑最开始的特殊情况
        三个指针
        然后隔一个换一次
        """
        if not head:
            return head
        
        exchangeFlag = 0
        temp0 = head
        temp1 = temp0.next
        if temp1:
            temp2 = temp1.next
        else:
            return head
  
        temp1.next = temp0
        temp0.next = temp2
        head = temp1
        
        # temp0 = temp0.next
        temp1 = temp0.next
        if temp1:
            temp2 = temp1.next
        else:
            return head
        exchangeFlag += 1

        while temp2:
            print(temp0.val,temp1.val,temp2.val,exchangeFlag % 2)
            if exchangeFlag % 2:
                temp0.next = temp2
                temp1.next = temp2.next
                temp2.next = temp1
            
            # 整体前进
            temp0 = temp0.next
            temp1 = temp0.next 
            temp2 = temp1.next
            
            exchangeFlag += 1
        
        return head
        
        



if __name__ == '__main__':
    solu = Solution()

    n5 = ListNode(5)
    n4 = ListNode(4,n5)
    n3 = ListNode(3,n4)
    n2 = ListNode(2,n3)
    n1 = ListNode(1,n2)

    result = solu.swapPairs(n1)

    while result:
        print(result.val)
        result = result.next

    # output_Str = 'result = ' + str(result)
    # print(output_Str)