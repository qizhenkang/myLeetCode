# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:58:54 2021

@author: qizhe
"""

import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        """
        感觉上不知道怎么做，看了答案
        意思是：
        1、要以合并2链表为基础，基本的思路是一个一个地合并嘛
        2、分治的思想是，配对合并，这样次数不变，但是每次的长度变短了
        3、利用一个优先级队列，一个一个地找最小值，合并到结果链表中
        """
        def mergeTwoLists(l1, l2):
            """
            标准写法
            """
            
            head = ListNode(-1)
            tail = head
            while l1 and l2:
                # print(l1.val,l2.val)
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
                
            tail.next = l1 if l1 else l2
            
            return head.next
        
        N = len(lists)
        if N == 0:
            return None
        elif N == 1:
            return lists[0]
        
        # 这里是不想用递归，就用了两个栈来来回倒腾
        stack1 = []
        stack2 = []
        
        for i in range(N):
            stack1.append(lists[i])
        
        while True:
            if len(stack1) == 1:
                break
            
            while stack1:
                if len(stack1) >= 2:
                    stack2.append(mergeTwoLists(stack1.pop(),stack1.pop()))
                else:
                    stack2.append(stack1.pop())
            while stack2:
                if len(stack2) >= 2:
                    stack1.append(mergeTwoLists(stack2.pop(),stack2.pop()))
                else:
                    stack1.append(stack2.pop())
                
        
        return stack1[0]

        
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List1 = ListNode(1)
    input_List1.next = ListNode(2)
    input_List1.next.next = ListNode(3)
    
    input_List2 = ListNode(4)
    input_List2.next = ListNode(5)
    # input_List2.next.next = ListNode(3)
    
    input_List3 = ListNode(1)
    # input_List3.next = ListNode(2)
    
    result = solu.mergeKLists([input_List1,input_List2,input_List3])
    
    
    while result:
        print(result.val)
        result = result.next

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    # output_Str = ' result = ' + str(result)
    # print(output_Str)