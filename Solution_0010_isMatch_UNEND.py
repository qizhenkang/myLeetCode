class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = True  # ! 默认为真，判断时置false
        s_Length = len(s)
        p_Length = len(p)
        pointer = 0
        last_p = str()  # ? 上一个字符
        continue_flag = 0
        for i in range(p_Length):
            if continue_flag:  # 跳过本次循环
                continue_flag = 0
                continue
            if pointer > s_Length - 1:
                result = False
                break
            p_i = p[i]
            if p_i == '.':  # todo 1 '.' 情况处理

                if i + 1 < p_Length:
                    if p[i + 1] == '*':  # todo 1.1'.*' 情况处理
                        continue_flag = 1
                        if i + 2 < p_Length:  # todo 1.1.1 '.*c'情况处理
                            while s[pointer] != p[i + 2]:
                                pointer = pointer + 1
                                if pointer >= s_Length:  # 意思是s已经找到最后了，此时进入下一个对p的循环就好了
                                    break
                                # 至此 s[pointer] == p[i + 2]
                                continue
                        else:  # todo 1.1.2 '.*_'情况处理
                            pointer = s_Length - 1
                            continue

                    else:  # todo 1.2 '.c' 情况处理
                        continue  # 意思是，此时本次判断结束，认为没问题
                else:   # todo '._' 情况处理
                    continue  # 意思是 此时匹配完成，认为没有错误

            elif p_i == '*':  # todo 2 '*' 情况处理
                continue  # * 意思是 '*' 一定是处理过的，不可以直接单独一个'*'

            else:  # todo 3 'c' 情况处理

                if i + 1 < p_Length:  # * 判断是否是最后一个元素

                    if p[i + 1] == '*':  # todo 3.1 'c*' 情况处理
                        # *这里必然要对s进行循环，是要找是否存在 0个/n个 c
                        while s[pointer] == p_i:  # 找第一个不为c的元素，如果没找到（全是c）也没问题
                            pointer = pointer + 1
                            if pointer >= s_Length:  # 意思是s已经找到最后了，此时进入下一个对p的循环就好了
                                break
                        continue
                        # 至此 s[pointer] != p_i

                    else:  # todo 3.2 'cc'情况处理
                        if s[pointer] == p_i:  # 判断是否相等
                            continue
                        else:
                            result = False  # 出现匹配不等的情况，直接结束，反馈错误
                            break

                else:  # todo 3.3 'c_'情况处理
                    if s[pointer] != p_i:  # 判断是否相等
                        continue
                    else:
                        result = False  # 出现匹配不等的情况，直接结束，反馈错误
                        break
                    # break  # 意思是 此时匹配完成，认为没有错误

        if pointer < s_Length:
            result = False

        return result


if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    input_Str_s = str('aaa')
    input_Str_p = str('aaa')
    # input_num = 11223
    output_Str = 'result = ' + str(solu.isMatch(input_Str_s, input_Str_p))
    print(output_Str)
