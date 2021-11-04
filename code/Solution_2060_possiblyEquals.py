# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:08:34 2021

@author: qizhe
"""

# import string
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        """
        感觉不难：
        1、对比的是数字长度
        2、简单的正则表达
        3、回溯即可
        """
        def __dfs(s1,s2,pointer1,pointer2,letters,currents1length,currents2length):
            print(pointer1,pointer2,currents1length,currents2length)
            if pointer1 >= len(s1) or pointer2 >= len(s2):
                print(pointer1,pointer2)
                print('length!!')
                if currents1length == currents2length:
                    return True
                return False
            if s1[pointer1] in letters and s2[pointer2] in letters:
                if currents1length == currents2length and s1[pointer1] == s2[pointer2]:
                    __dfs(s1,s2,pointer1+1,pointer2+1,letters,currents1length+1,currents2length+1)
                else:
                    
                    return False
            # if s1[pointer1] not in letters: #or s2[pointer2] not in letters:
            #     addlength = 0
            #     for i in range(pointer1,len(s1)):
            #         if s1[i] not in letters:
            #             addlength *=10
            #             addlength += s1[i]
            #         __dfs(s1,s2,pointer1+addlength,pointer2,letters)
            if s2[pointer2] not in letters: #or s2[pointer2] not in letters:
                addlength = 0
                for i in range(pointer2,len(s2)):
                    if s2[i] not in letters:
                        addlength *=10
                        addlength += int(s2[i])
                        print(addlength)
                        __dfs(s1,s2,pointer1,i+1,letters,currents1length,currents2length+addlength)
                    else:
                        break
            return
        
        
        # def __dfs_s1length(s1,pointer1,letters,s1length,currentlength,s1DictList,currentDict):
        #     if pointer1 >= len(s1):
        #         s1length.append(currentlength)
        #         s1DictList.append(currentDict)
        #         return
        #     if s1[pointer1] in letters:
        #         currentDict[currentlength] = s1[pointer1]
        #         print(currentDict)
        #         __dfs_s1length(s1,pointer1+1,letters,s1length,currentlength+1,s1DictList,currentDict)
        #         del currentDict[currentlength]
        #         # print(currentDict)
        #     if s1[pointer1] not in letters:
        #         addlength = 0
        #         for i in range(pointer1,len(s1)):
        #             if s1[i] not in letters:
        #                 addlength *=10
        #                 addlength += int(s1[i])
        #                 __dfs_s1length(s1,i+1,letters,s1length,currentlength+addlength,s1DictList,currentDict)
        #             else:
        #                 break
        #     return
        letters = set('abcdefghijklmnopqrstuvwxyz')
        pointer1 = 0
        pointer2 = 0
        s1length = []
        s2length = []
        s1DictList = []
        __dfs(s1,s2,0,0,letters,0,0)
        # __dfs_s1length(s1,0,letters,s1length,0,s1DictList,{})
        # print(s1length,s1DictList)
        # __dfs_s1length(s2,0,letters,s2length,0)
        
        # okFlag = 0
        # for i in s1length:
        #     if i in s2length:
        #         okFlag = 1
        #         break
        # print(s1length,s2length)
        # if not okFlag:
        #     # 长度不同，返回否
        #     return False

        return s1length
    
if __name__ == '__main__':
    solu = Solution()
    # distance = [2,1,1,2]
    # distance = [1,2,3,4]
    # nums = ["Hello","Alaska","Dad","Peace"]
    
    nums = [1,3]
    start = 6
    goal = 4
    
    s1 = "internationalization"
    s2 = "i18n"

    result = solu.possiblyEquals(s1,s2)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)