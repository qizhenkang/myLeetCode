# -*- coding: utf-8 -*-
"""
Created on 2022/08/15 16:42:47

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


# Definition for a Node.
from typing import Dict, List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self) -> str:
        return str(self.val) + ' id: ' + str(id(self))

    def __repr__(self) -> str:
        return self.__str__()


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        很奇怪的一个题，做的时候身体不舒服

        卡在了一个 neighbors 需要重新放置 而不能 = neighbors


        """

        if not node:
            return None

        hash_dict: Dict[Node, Node] = {}

        stack: List[Node] = [node]
        while stack:
            # print(stack)
            # print(hash_dict)

            nd = stack.pop(0)
            nd_new = Node(val=nd.val)
            nd_new.neighbors = [i for i in nd.neighbors]
            hash_dict[nd] = nd_new

            for i in range(len(nd.neighbors)):
                neighbor = nd.neighbors[i]
                if neighbor not in hash_dict:
                    stack.append(neighbor)

        memo = []
        stack: List[Node] = [hash_dict[node]]
        while stack:
            nd = stack.pop(0)
            # print(nd, nd.neighbors)
            for i in range(len(nd.neighbors)):
                if nd.neighbors[i] in hash_dict:
                    nd.neighbors[i] = hash_dict[nd.neighbors[i]]

            for i in range(len(nd.neighbors)):
                neighbor = nd.neighbors[i]
                if neighbor not in memo:
                    stack.append(neighbor)
                    memo.append(neighbor)

        return hash_dict[node]


if __name__ == '__main__':
    solu = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    a = solu.cloneGraph(node1)
