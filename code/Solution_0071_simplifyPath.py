# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:00:22 2021

@author: qizhe
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        读题：
        1、这种涉及字符串的题一直不太会做，这里整理一下题目的要求
        2、始终以斜杠 '/' 开头。两个目录名之间必须只有一个斜杠 '/' 。最后一个目录名（如果存在）不能 以 '/' 结尾。
        3、中间不能含'.'
        4、感觉用栈/队列比较好，读目录嘛，是吧
        
        测试：
        1、一次通过，但性能一般
        
        用时18min
        
        """
        N = len(path)
        nameFlag = 1
        currentName = ''
        nameStack = []
        for i in range(N):
            if path[i] == '/' or i == N-1:
                # 防止最后一个不是 / 
                if i == N-1 and path[i] != '/':
                    currentName += path[i]
                nameFlag = 1
                # 判断栈
                if currentName:
                    if currentName == '.':
                        # 什么都不做
                        pass
                    elif currentName == '..':
                        # 弹出一个
                        if nameStack:
                            nameStack.pop()
                    else:    
                        # 正常名称，加入
                        nameStack.append(currentName)
                    currentName = ''
                continue
            # 是否为新元素
            if nameFlag:
                currentName += path[i]
        
        # 读栈
        validPath = ''
        for st in nameStack:
            validPath += '/' + st
        # 根目录
        if not validPath:
            validPath = '/'
        return validPath

        
if __name__ == '__main__':
    solu = Solution()
    
    arr = "/a/./b/.././c"
    # arr = '/home//foo/'
    # arr = '/../'
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # input_List = 1

    result = solu.simplifyPath(arr)

    output_Str = ' result = ' + str(result)
    print(output_Str)