# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:35:15 2021

@author: qizhe
"""

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        读题：
        1、基本思路没问题，就是保存头部，逐个换指针
        
        测试：
        1、一次通过，15min，性能良好
        
        答案：
        
        """
        headpre = ListNode(-1,head)
        leftpre = headpre
        pointer = head
        pointerlast = headpre
        # pointerlast = headpre
        cnt = 1
        if left == right:
            return head
        while pointer:
            if cnt == left:
                leftpre = pointerlast
            
            if cnt == right:
                leftpre.next.next = pointer.next
                leftpre.next = pointer

            if cnt >= left:
                # 实现指针反向
                temp = pointer
                pointer = pointer.next
                temp.next = pointerlast
                pointerlast = temp
            else:
                pointerlast = pointer
                pointer = pointer.next
            
            if cnt == right:
                break
            
            cnt += 1
            
        return headpre.next
    
if __name__ == '__main__':
    solu = Solution()
    head0 = ListNode(6)
    head1 = ListNode(5,head0)
    head2 = ListNode(4,head1)
    head3 = ListNode(3,head2)
    head4 = ListNode(2,head3)
    head5 = ListNode(1,head4)
    # x = 3
    result = solu.reverseBetween(head5,5,6)
    while result:
        print(result.val, end='-> ')
        result = result.next