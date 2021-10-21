# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:18:04 2021

@author: qizhe
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        读题：
        1、感觉不难，就是链表的排序
        2、思路是，逐点扫描，小于x的一列，大于等于x的一列
        3、两列合并
        
        测试：
        1、一次通过，性能一般，用时15min
        2、看完答案，发现思路一模一样，原代码又提交一遍，性能超好
        
        答案：
        1、和答案一模一样
        """
        leftHead = ListNode()
        rightHead = ListNode()
        leftPointer = leftHead
        rightPointer = rightHead
        while head:
            # print(head.val)
            if head.val < x:
                # print(leftPointer.val,head.val)
                leftPointer.next = head
                leftPointer = head
            else:
                # print(rightPointer.val,head.val)
                rightPointer.next = head
                rightPointer = head
            head = head.next
        
        leftPointer.next = rightHead.next
        rightPointer.next = None
        # print(leftPointer.val,rightHead.next.val)
        return leftHead.next

        
if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]

    n = 8
    inputList = [1]
    inputList = [2, 0, 5, 6, 2, 3]
    matrix = [["0","1","0","1","0"],["1","1","0","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = []
    matrix = [["0"],['1']]
    matrix = [["1","0"]]
    # inputList = [2, 2]
    # time = 3
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    head0 = ListNode(2)
    head1 = ListNode(5,head0)
    head2 = ListNode(2,head1)
    head3 = ListNode(3,head2)
    head4 = ListNode(4,head3)
    head5 = ListNode(1,head4)
    x = 3
    result = solu.partition(head5,x)
    while result:
        print(result.val)
        result = result.next
    # output_Str = ' result = ' + str(result)
    # print(output_Str)