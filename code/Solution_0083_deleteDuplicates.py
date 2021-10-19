# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:33:53 2021

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
        2、确实利用了双指针，一个是扫描的，一个是记录每个数字第一个数
    
        
        测试：
        1、一次通过，用时5分钟，存储性能好，但用时明显可以优化
        """
        if not head:
            return head

        # pointer = head
        # 每个数字第一个数
        # headpre = ListNode(101,head)
        firstPointer = head
        lastNum = head.val
        # 是否删除
        deleteFlag = False
        pointer = head.next
        while pointer:
            print(lastNum,pointer.val,firstPointer.val)
            if pointer.val == lastNum:
                deleteFlag = True
            else:
                if deleteFlag:
                    firstPointer.next = pointer
                    deleteFlag = False
                firstPointer = pointer
                lastNum = pointer.val
            if not pointer.next and deleteFlag:
                firstPointer.next = None
            pointer = pointer.next
        
        return head

        
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
    # head5 = ListNode(2)
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