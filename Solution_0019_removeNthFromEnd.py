# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:19:50 2021

@author: qizhe
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 一遍成功，就是用了两个指针就做出来了。

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 进阶要求是一趟扫描实现，那么就需要两个指针，然后这两个指针之差为n就可以了
        # 1为前面指针，2为后面指针，2比1滞后n个
        
        pointer1 = head 
        pointer2 = head
        for i in range(n-1):
            pointer1 = pointer1.next
        # 防止删除的就是第1个
        if not pointer1.next:
            return head.next
        # 需要删除的前1个
        # 这里的一个小技巧，让1在指向最后一个时停住
        # 这时候2，不要再往前走了
        
        while(1):
            pointer1 = pointer1.next
            # 如果pointer 1是最后一个了，2不要再往前走了
            if not pointer1.next:
                break
            pointer2 = pointer2.next
        
        # 此时pointer2是要删除的前一个
        pointer2.next = pointer2.next.next
        
        return head

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('{[]{}()}')
    # input_list =
    input_List = [90]
    input_int = 200
    n1 = ListNode(1, None)
    n2 = ListNode(2, n1)
    n3 = ListNode(3, n2)
    n4 = ListNode(4, n3)
    n5 = ListNode(5, n4)
    
    n = 1

    result = solu.removeNthFromEnd(n1, n)

    while(result):
        print(result.val)
        result = result.next
    # output_Str = 'result = ' + solu.intToRoman(input_int)
    # output_Str = 'result = ' + str(result.val)
    # print(output_Str)
