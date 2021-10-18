# Search

一切皆可搜索。

深度优先搜索、回溯法、广度优先搜索。

## Depth-First Search

深度优先搜索比较常用的是用递归来做。但软件工程中递归不多见，主要是怕难以理解/栈溢出。

递归的本质是栈，所以可以考虑直接用个栈来实现。

## Backtracking

回溯已经比较熟了，核心是一个"恢复现场"的概念。

## Breadth-First Search

周赛 263 最后一题考到了图的最短路程，没做出来，这次整理一下。

广度优先搜索还不是很熟，可以依赖深度优先搜索来考虑。

**深度优先搜索**的本质是**栈**，而**广度优先搜索**是**队列**。

因此，做了一下 _LeetCode_ [126.findLadders](../code/Solution_0126_findLadders.py) 和 _LeetCode_ [127.ladderLength](../code/Solution_0127_ladderLength.py) 题。它们是典型的的找最短路径的题目。
其中，BFS 用来建图。

广度优先搜索，本质上是一个队列，每次循环本层出队，与此同时下一层入队，不断循环直至队列为空。

<!-- [^5]: Some unrecorded data for some reason. -->
