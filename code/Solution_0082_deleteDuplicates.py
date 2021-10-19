# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:05:17 2021

@author: qizhe
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        读题：
        1、一看就简单，只需要双指针就可以吧？
        2、确实利用了双指针，一个是扫描的，一个是记录上一个数字的最后一个数
        3、为了保持一致，多加了一个头部元素
        
        测试：
        1、一次通过，性能很好
        """
        if not head:
            return head

        pointer = head
        # 上一个数字的最后一个
        headpre = ListNode(101,head)
        lastPointer = headpre
        lastNum = 101
        # 是否删除
        deleteFlag = False
        while pointer:
            # print(lastNum,pointer.val,lastPointer.val)
            if pointer.val == lastNum:
                deleteFlag = True
            else:
                deleteFlag = False
            
            if pointer.next and pointer.next.val != pointer.val:
                if deleteFlag:
                    lastPointer.next = pointer.next
                else:
                    lastPointer = pointer
            if pointer and not pointer.next and deleteFlag:
                lastPointer.next = None
            
                
            lastNum = pointer.val
            pointer = pointer.next
        
        return headpre.next

        
if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]
    n = 8
    # edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    # time = 3
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","cot",'cog']
    # wordList = ["hot","dot","dog","lot","log","cog"]
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    # head5 = ListNode(3)
    # head4 = ListNode(2,head5)
    head3 = ListNode(1)
    head2 = ListNode(1,head3)
    head1 = ListNode(1,head2)
    
    result = solu.deleteDuplicates(head1)
    # output_Str = ' result = ' + str(result)
    print(' result = ',end=' ')
    while result:
        print(result.val,end='-> ')
        result= result.next
    
    # print(output_Str)