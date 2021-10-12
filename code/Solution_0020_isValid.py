import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 解题思想
# 实际上，括号匹配就是栈的典型应用，这里用到了括号的特点，当出现左括号时入栈，当出现右括号时判断，判断不过立即返回，提高效率
# 2021/08/10


class Solution:
    def isValid(self, s: str) -> bool:
        # 主要思想为栈，从而匹配括号
        result = False
        myStack = []

        # 左右变换字典
        self.dict_trans = {')': '(', ']': '[', '}': '{'}
        # 左右判断字典
        self.dict_LR = {'(': 0, '[': 0, '{': 0,
                        ')': 1, ']': 1, '}': 1}
        breakFlag = False
        for l in s:
            # 栈判断
            logger.debug(myStack)
            if self.dict_LR[l] == 0:
                # 左括号，入栈
                myStack.append(l)
            else:
                # 右括号，判断
                if myStack:
                    # logger.debug(
                    #     ['compare: ', myStack[-1], self.dict_trans[l]])
                    if myStack[-1] == self.dict_trans[l]:
                        # 出栈
                        myStack.pop()
                    else:
                        # 右括号未匹配，直接结束
                        breakFlag = True
                        break
                else:
                    # 第一个就是右括号，直接结束
                    breakFlag = True
                    break

        # 若栈为空且未break，则输出真
        if not myStack and not breakFlag:
            result = True

        return result

    # def isMatch(self, left, right):
    #     matchFlag = False
    #     if self.diction[left] == right:
    #         matchFlag = True

    #     return matchFlag


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('{[]{}()}')
    # input_list =
    input_List = [90]
    input_int = 200

    result = solu.isValid(input_Str)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
