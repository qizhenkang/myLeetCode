# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:59:50 2021

@author: qizhe
"""

# Below is the interface for Iterator, which is already defined for you.

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    """
    没太懂这题要考啥，看了答案。
    好像是一个“设计”类的题？
    """
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._next = iterator.next()
        self._hasNext = iterator.hasNext()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next
        

    def next(self):
        """
        :rtype: int
        """
        ret = self._next
        self._hasNext = self.iterator.hasNext()
        self._next = self.iterator.next() if self._hasNext else 0
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._hasNext
        
if __name__ == '__main__':
    # solu = Solution()
    # nums = ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
    # Your PeekingIterator object will be instantiated and called as such:
    nums = [[[1, 2, 3]], [], [], [], [], []]
    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        val = iter.peek()   # Get the next element but not advance the iterator.
        iter.next()         # Should return the same value as [val].
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    # result = solu.groupAnagrams(strs)

    # output_Str = ' result = ' + str(result) 
    # print(output_Str)

