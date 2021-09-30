# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:57:16 2021

@author: qizhe
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        """
        这是一个广度优先遍历
        第一反应是要迭代遍历，然后每层建立一个队列
        """
        
        if not root:
            return root
        
        queue = [root]
        
        while queue:
            
            n = len(queue)
            # prevNode = None
            
            # 每层遍历
            for i in range(n):
                # 出队
                tempNode = queue.pop(0)
                
                if i < n-1:
                    tempNode.next = queue[0]
                    print(tempNode.val,tempNode.next.val)
                
                # if i > 0:
                #     # print(prevNode.val,tempNode.val)
                #     prevNode.next = tempNode
                
                # 下层入队
                if tempNode.left:
                    queue.append(tempNode.left)
                if tempNode.right:
                    queue.append(tempNode.right)
                
                # prevNode = tempNode
        
        return root
        
        
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    # input_List = ['RLRRLLRLRL','RL','RLRRRLLRLL','']
    input_List = Node(3)
    input_List.left = Node(9)
    input_List.left.left = Node(1)
    input_List.left.right = Node(2)
    input_List.right = Node(20)
    input_List.right.left = Node(15)
    input_List.right.right = Node(7)
    # for i in input_List:

    result = solu.connect(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)
        