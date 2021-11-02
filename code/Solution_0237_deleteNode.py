
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        读题：
        1、昨晚睡觉没睡着看了一下，不会，看了一下答案，今天早上来写
        
        测试：
        一次通过，但性能不好
        
        答案：
        1、答案更简单，只需要删除下一个，两行结束
        """
        node.val = node.next.val
        node.next = node.next.next
        # pointer = node.next
        # while pointer:
        #     node.val = pointer.val
        #     node = pointer
        #     pointer = pointer.next
            
        



if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    # input_Str = str('LEETCODEISHIRING')
    input_num = 11223
    output_Str = 'result = ' + str(solu.reverse(input_num))
    print(output_Str)
