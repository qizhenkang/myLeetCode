class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        gap_flag = 1
        sign_flag = 1

        for i in s:
            asc_i = ord(i)
            if i == ' ':  # todo 读取到空格
                if gap_flag:  # ? 判断现在是否还在句首
                    continue  # * 还在句首，继续寻找
                else:
                    break  # *不在句首，终止循环
            else:
                gap_flag = 0  # ? 关闭此通道，意思是 已经出现了非空格元素（不是句首了
                if i == '+' or i == '-':  # ? 判断是否是符号
                    if sign_flag:  # * 第一次读取到符号
                        sign_flag = 0  # 关闭通道
                        if i == '+':  # todo 判断符号
                            sign = 1
                        else:
                            sign = -1
                    else:
                        break  # * 多次读取到符号，弹出
                elif asc_i >= 48 and asc_i <= 57:  # todo 读取到数字
                    sign_flag = 0  # 关闭通道
                    result = result * 10 + asc_i - 48
                else:  # todo 读取到奇奇怪怪的没用符号
                    break

        result = result * sign
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648

        return result


if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    input_Str = str('    -42  3sd')
    # input_num = 11223
    output_Str = 'result = ' + str(solu.myAtoi(input_Str))
    print(output_Str)
