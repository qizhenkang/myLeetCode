# LeetCode Weekly Contest

## Abstract

周赛有一些注意事项，这里简要记录一下：

1. 通过 + 短时间是本质，其他的不重要
2. 编辑器什么的尽可能减少时间浪费

## Weekly Contest Records

### Weekly Contest 265

做出来了 3 道题，感觉比较稳定了，没遇到大的麻烦。

第一题，一次通过。

第二题，错了一次，是因为没有求最小，细节代码修改后通过

第三题，错了两次，本质原因是因为对于 BFS 掌握不够熟练。
第一个错是超时，是因为把越界数入栈了，逻辑上没问题，但复杂度不行，改成提前判断越界
第二个错是逻辑错，是因为提前判断越界后，导致本层的最短路径没有算完就返回了下一层。
修改后通过。

重判第三题给我 WA 了，导致名次从 500 变成了 1400，仔细看了一下，发现有一个复制的时候 num1 没有修改为 num2，修改后通过，惨惨，以后提交一定要检查清楚的。

第四题，就没做来，思路不够清楚。

### Weekly Contest 264

这次懵懵的，只做出来了第一题。第二题大家都是暴力搜索的，而我想拼起来，做麻烦了

第三题没读懂**二叉树的编号规则**。

### Weekly Contest 263

30min 做出了 3 题，卡在了第四题。要用到 BFS，没有做出来，赛后补了一下 BFS 的知识。

### Weekly Contest 262

第一次参赛，做出来了两个题。
