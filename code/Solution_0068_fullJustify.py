# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:24:56 2021

@author: qizhe
"""

class Solution:
    def fullJustify(self, words, maxWidth: int):
        """
        有点复杂，本质上是用了双指针，一段一段地确定，没什么好办法
        """
        result = []
        # 双指针
        p1 = 0
        p2 = 0
        # 记录当前段/是否为最后段
        currentlenth = 0
        finalFlag = 0
        wordslength = len(words)
        
        # 结束条件为p1到达最后
        while p1 < wordslength:
            
            # p2确定当前段文字
            while currentlenth + p2 - p1 -1 <= maxWidth:
                
                if p2 >= wordslength:
                    finalFlag = 1
                    break
                
                currentlenth += len(words[p2])
                p2 += 1

            # 最后一段特殊处理 防止越界
            
            # print(p1,p2)
            
            # p1确定当前段排布
            # 需要确定：
            # 1、总字数/总空格数
            # 2、每个空格数

            if finalFlag:
                currentstr = words[p1]
                p1 +=1
                while p1 < p2:
                    currentstr += ' ' + words[p1]
                    p1 +=1
                currentstr += ' ' * (maxWidth-len(currentstr))
                
            else:
                p2 -= 1
                currentlenth -= len(words[p2])
                # 总空格数
                totalspace = maxWidth - currentlenth
                # 总空位置数
                totalposi = p2 - p1 - 1
                if totalposi > 0:
                
                    # 每空空格数
                    currentspace = totalspace // totalposi
                    spaces = [currentspace] * totalposi
                    
                    # print(totalspace,totalposi,spaces)
                    
                    for i in range(totalspace % totalposi):
                        spaces[i] += 1
    
                    i = 0
                    currentstr = words[p1]
                    p1 +=1
                    for i in range(totalposi):
                        currentstr += ' '*spaces[i] + words[p1]
                        p1 +=1
                else:
                    currentstr = words[p1] + ' '*totalspace
                    p1 += 1

            result.append(currentstr)
            
            currentlenth = 0
            p1 = p2
        
        return result
    
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    input_List = ["This", "is", "an", "example", "of", "text", "justification."]
    # input_List = ["What","must","be","acknowledgment","shall","be"]
    # input_List = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]



    result = solu.fullJustify(input_List,16)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)
    