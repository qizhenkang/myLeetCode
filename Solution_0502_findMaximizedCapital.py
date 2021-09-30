# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:53:18 2021

@author: qizhe
"""
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        """
        数据量较大，用到排序思想
        
        本质上，就是有两组数，按照其中一个排序，然后在满足条件当中选另一个最优
        
        非常像，先选可行解，再在可行解中选最优值

        Parameters
        ----------
        k : int
            DESCRIPTION.
        w : int
            DESCRIPTION.
        profits : TYPE
            DESCRIPTION.
        capital : TYPE
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        # 资本足够多，直接选最大
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))
        
        # 合成元组，进行排序，升序
        tulpelist = [(profits[i],capital[i]) for i in range(len(capital))]
        tulpelist.sort(key = lambda x:(x[1])) # 按照成本升序
        
        crr = 0 # 指针，只遍历一次
        heap = []
        # 进行k次决策
        for _ in range(k):
            
            # 最大的改进，是crr只读一次
            # 利用了大根堆的数据结构，通过成本排序，crr向上读，读到不能接受的成本
            # 即为当前可以接受的所有项目，然后选一个最大利润的
            # 如果没有可以接受的，就直接返回
            while crr < len(capital) and w >= tulpelist[crr][1]:
                heapq.heappush(heap,-tulpelist[crr][0]) # 默认是最小堆，
                crr += 1

            if heap:
                w -= heapq.heappop(heap)
            else:
                break
            
        
        return w


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    input_List = [1,1,1,5,3]
    # input_List = ['RLRRLLRLRL','RL','RLRRRLLRLL','']
    # input_List = TreeNode(3)
    # input_List.left = TreeNode(9)
    # input_List.right = TreeNode(20)
    # input_List.right.left = TreeNode(15)
    # input_List.right.right = TreeNode(7)
    # for i in input_List:

    result = solu.findMaximizedCapital(2,0,[1,2,3],[0,1,1])

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)
    