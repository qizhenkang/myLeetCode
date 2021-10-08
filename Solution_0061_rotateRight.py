# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:20:24 2021

@author: qizhe
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        """
        读题：
        1、读题读错了，人家是倒着选择，从后往前k个
        """
        if k == 0 or not head:
            return head
        cnt = 0
        temp = head
        while temp:
            temp = temp.next
            cnt +=1
        if k%cnt == 0:
            return head
        k = cnt - k%cnt
        
        # preHead = ListNode(-1,head)
        cnt = 1
        temp = head
        newhead = head
        while cnt < k and temp.next:
            temp = temp.next
            cnt +=1
        print(k,cnt)
        if not temp.next:
            print(k,cnt,k%cnt)
            k %= cnt()
            cnt = 1
            temp = head
            while cnt < k and temp.next:
                temp = temp.next
                cnt +=1
        
        if temp.next:
            newhead = temp.next
            temp.next = None
            temp = newhead
            while temp.next:
                temp = temp.next
            temp.next = head
        else:
            newhead = head

        return newhead
        
        
if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    intervals = "Hello, my name is John"
    n5 = ListNode(5)
    n4 = ListNode(4,n5)
    n3 = ListNode(3,n4)
    n2 = ListNode(2,n3)
    n1 = ListNode(1,n2)
    # n0 = ListNode(0,n1)
    k = 2
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solu.rotateRight(n1,k)
    # output_Str = ' result = '
    print(' result = ',end=' ')
    while result:
        print(result.val,end=' ')
        result = result.next
        

    # output_Str = ' result = ' + str(result) 
    # print(output_Str)