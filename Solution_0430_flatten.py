# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 10:11:56 2021

@author: qizhe
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next1, child):
        self.val = val
        self.prev = prev
        self.next = next1
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        """
        扁平化多级双向链表，把多级变成一级的双向链表

        """
        
        tempPointer = head
        parentPointers = [] # 维护一个指针栈
        while tempPointer:
            # 看看是否存在下一级
            print(tempPointer.val)
            if tempPointer.child:
                # 存在下级
                # 保存上级
                parentPointers.append(tempPointer)
                # 进入下级
                tempPointer = tempPointer.child
            else:     
                # 不存在下级
                # 看看是否存在next
                if tempPointer.next:
                    # 存在next
                    tempPointer = tempPointer.next
                else:
                    # 不存在next（可能是全部结束了，也可能是子级结束了）
                    if parentPointers:
                        
                        while parentPointers:
                            parentPointer = parentPointers.pop()
                            # print('--',parentPointer.val,tempPointer.val)
                            if parentPointer.next:
                                # print('---',parentPointer.val,tempPointer.val)
                                tempPointer.next = parentPointer.next
                                parentPointer.next.prev = tempPointer
                                tempPointer = parentPointer.next
                                
                                parentPointer.child.prev = parentPointer
                                parentPointer.next = parentPointer.child
                                parentPointer.child = None
                                break
                            else:
                                parentPointer.child.prev = parentPointer
                                parentPointer.next = parentPointer.child
                                parentPointer.child = None

                    else:
                        tempPointer = None
                        
                    
                
        print('------一次正向遍历--------')
        temphead = head
        # tempend = head
        while temphead:
            print(temphead.val)
            if not temphead.next:
                tempend = temphead
                
            temphead = temphead.next
        print('------一次反向遍历--------')
        while tempend:
            print(tempend.val)
            tempend = tempend.prev

        return head
    
    
if __name__ == '__main__':
    solu = Solution()
    
    input_List = Node(1,None,None,None)
    input_List.next = Node(2,input_List,None,None)
    input_List.child = Node(3,None,None,None)
    input_List.child.next = Node(4,input_List.child,None,None)
    input_List.child.next.next = Node(6,input_List.child.next,None,None)
    input_List.child.next.child = Node(5,None,None,None)
    
    result = solu.flatten(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)