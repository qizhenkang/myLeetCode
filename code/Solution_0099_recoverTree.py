# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:20:28 2021

@author: qizhe
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        
        第一反应还是中序遍历，然后判断顺序。
        
        二次读题：
        1、感觉像是一个二叉树的排序算法，要求不改变结构，就很像中序遍历+冒泡排序
        2、尝试一下递推栈，没那么简单，感觉不好下手
        3、思路上，就是二叉树的排序，需要中序遍历，需要交换位置
        4、只有两个节点被交换位置了，应该还简单一点
        
        感觉没有很好的方法
        
        答案:
        1、答案推荐了一种'morris'算法，评论都说“大名鼎鼎”
        
        所以，这个题就当练习一下Morris算法吧：
        简介：
        1、morris遍历利用的是树的叶节点左右孩子为空（树的大量空闲指针），实现空间开销的极限缩减
        2、建立一种机制，对于没有左子树的节点只到达一次，对于有左子树的节点会到达两次
        
        测试：
        1、超时了，没搞清楚是为什么
        2、没有特别清楚为什么超时了，没有找到原因，改了一个break就好了
        """
        
        # morris算法
        pre = None
        former = None
        latter = None
        while root:
            # print('start: ',root.val)
            # if pre:
            #     print('         ',pre.val)
            
            # pre = root
            # 首先判断是否存在左孩子
            if root.left:
                predecessor = root.left
                # 寻找左子树中最右节点（也可以是左子树根节点）
                # 其实就是，找最右点，也就是左子树中序遍历的最后一个点
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                # 最右点，要么是空，则建立；要么是root，则说明已经走过
                if predecessor.right: 
                    # 如果存在，则说明之前已经搭好桥了，这一步需要拆桥，因为需要还原树结构
                    predecessor.right=None
                else: 
                    # 此一步为搭桥，这样就可以直接找到root
                    predecessor.right = root
                    root = root.left
                    continue
            # 这里设计的非常精妙，向左走的不过来，向右走的才过来
            
            # if pre:
                # print(pre.val)
            if pre and pre.val > root.val:
                # print(pre.val,root.val)
                latter = root
                if not former:
                    former = pre
                else:
                    print(latter.val,former.val)
                    break

            pre = root
            root = root.right
        # print(former.val, latter.val)
        print(latter.val,former.val)
        if former and latter: 
            former.val, latter.val = latter.val, former.val
        # return
        # [5,0,8,2,-5,6,9]
        # [10,5,15,0,8,13,20,2,-5,6,9,12,14,18,25]



if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    input_List = TreeNode(5)
    input_List.left = TreeNode(0,TreeNode(2),TreeNode(-5))
    input_List.right = TreeNode(8,TreeNode(6),TreeNode(9))
    
    result = solu.recoverTree(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)