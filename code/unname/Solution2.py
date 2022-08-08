# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:32:09 2021

@author: qizhe
"""


from typing import List
from collections import defaultdict
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head) -> List[int]:
        
        result = [-1,-1]
        if not head:
            return result
        lastNum = head.val
        head = head.next
        minPoints = []
        minDistance = 1e6
        i = 1
        while head:
            # print(i,head.val,lastNum)
            if head.next and (lastNum < head.val and head.val > head.next.val or lastNum > head.val and head.val < head.next.val):
                minDistance = min(minDistance,i - minPoints[-1]) if minPoints else 1e6
                minPoints.append(i)
            lastNum = head.val
            i += 1
            head = head.next
        print(minPoints)
        if len(minPoints) < 2:
            return result
        result[1] = minPoints[-1] - minPoints[0]
        result[0] = minDistance
        return result


if __name__ == '__main__':
    solu = Solution()
    # distance = [2,1,1,2]
    # distance = [1,2,3,4]
    nums = ListNode(6,ListNode(8,ListNode(4,ListNode(1,ListNode(9,ListNode(6,ListNode(6,ListNode(10,ListNode(6,)))))))))
    result = solu.nodesBetweenCriticalPoints(nums)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)