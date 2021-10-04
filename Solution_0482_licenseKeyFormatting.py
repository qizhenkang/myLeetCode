# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:24:43 2021

@author: qizhe
"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        题目有点麻烦：
        1、给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。
        2、特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1 个字符。
        3、两个分组之间需要用 '-'（破折号）隔开，
        4、并且将所有的小写字母转换为大写字母。
        
        这个题麻烦在于，他把第一个当成了可变的。
        """
        totalNumber = len(s)
        dashNumber = 0
        for i in s:
            if i == '-':
                dashNumber += 1
        k1 = (totalNumber - dashNumber) % k if dashNumber else k
        if not k1:
            k1 = k
        print(totalNumber,dashNumber,k1)
        result = ''
        k1Flag = 1
        cnt = 0
        for i in s:
            if i == '-':
                continue
            else:
                if 'a'<= i <= 'z':
                    i = chr(ord('A') - ord('a') + ord(i))
                result += i 
                cnt += 1
            
            if k1Flag:
                if cnt == k1:
                    result += '-'
                    cnt = 0
                    k1Flag = 0
                
            else:
                if cnt == k:
                    result += '-'
                    cnt = 0
        if not result:
            return ''
        if result[-1] == '-':
            result = result[:-1]

        return result

if __name__ == '__main__':
    solu = Solution()
    
    # s = "5F3Z-2e-9-w"
    # k = 4
    s = "2-5g-3-J"
    k = 2
    s = "2-4A0r7-4k"
    k = 3
    s = '2'
    k = 2
    result = solu.licenseKeyFormatting(s,k)

    output_Str = ' result = ' + str(result)
    print(output_Str)