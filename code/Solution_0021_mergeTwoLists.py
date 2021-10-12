# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:19:50 2021

@author: qizhe
"""

# Definition for singly-linked list.

# 思路基本是正确的，就是不如答案简洁
# 迭代的思路，一个一个地比较l1和l2头部，然后加入新的


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        标准写法
        """
        head = ListNode(-1)
        tail = head
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        tail.next = l1 if l1 else l2
        
        return head.next
            
            
            

        # 法1：读为list，然后list写为linked list
        # # 读链表
        # list_l1 = self.readLists(l1)
        # list_l2 = self.readLists(l2)
        # # 合并列表
        # resultList = list_l1 + list_l2
        # # 列表排序
        # resultList.sort()
        # # 写链表
        # result = self.writeLists(resultList)

        # # 法2：一个一个读到新的linked list
        # if l1 or l2:
        #     EndFlag = 0
        #     firstFlag = 1
        #     while(not EndFlag):
        #         resultNode, EndFlag, l1, l2 = self.readNextNode(l1, l2)
        #         if firstFlag:
        #             result = resultNode
        #             tempNode = result
        #             firstFlag = 0
        #         else:
        #             tempNode.next = resultNode
        #             tempNode = tempNode.next
        # else:
        #     result = None

        # 法3 ： 一个一个读，不开新的Linked list

        # return result

    def readNextNode(self, l1, l2):
        EndFlag = 0
        if l1 and l2:

            # 找小的先加入
            if l1.val < l2.val:
                resultNode = l1
                l1 = l1.next
            else:
                resultNode = l2
                l2 = l2.next

        elif l1:
            resultNode = l1
            EndFlag = 1
        elif l2:
            resultNode = l2
            EndFlag = 1
        else:
            resultNode = None
            EndFlag = 1

        return resultNode, EndFlag, l1, l2

    # 读链表
    def readLists(self, l1: ListNode):
        relist = []
        temp_list = l1
        # 非空才进行
        while(temp_list):
            relist.append(temp_list.val)
            temp_list = temp_list.next

        return relist
    # 写链表

    def writeLists(self, list):

        # 非空
        if list:
            relist = ListNode()
            temp_Val = list.pop(0)
            relist.val = temp_Val
            temp_pointerNode = relist

            while(list):
                temp_newNode = ListNode()
                temp_newNode.val = list.pop(0)
                temp_pointerNode.next = temp_newNode
                temp_pointerNode = temp_newNode

        else:
            relist = None

        return relist


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('{[]{}()}')
    # input_list =
    input_List = [90]
    input_int = 200
    n1 = ListNode(8, None)
    n2 = ListNode(7, n1)
    n3 = None

    n4 = ListNode(5, None)
    n5 = None

    result = solu.mergeTwoLists(n2, n4)

    while result:
        print(result.val)
        result = result.next
    # output_Str = 'result = ' + solu.intToRoman(input_int)
    # output_Str = 'result = ' + str(result)
    # print(output_Str)
