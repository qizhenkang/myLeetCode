# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 09:50:46 2021

@author: qizhe
"""

class SummaryRanges:
    
    """
    做题时提出了一个buffer的思路，但超时了，看来还需要更合理的buffer
    
    答案：
    万万没想到，不需要buffer 就正常处理就做出来了
    """
    def __init__(self):
        self.intervals = []
        # self.buffer = []


    def addNum(self, val: int):

        N = len(self.intervals)
        if N ==0:
            self.intervals.append([val,val])
            return
        # endFlag = 0
        for j in range(N):
            # print(b,self.intervals[j])
            if self.intervals[j][0] <= val <= self.intervals[j][1]:
                break
            elif j<N-1 and val == self.intervals[j][1] +1 and val == self.intervals[j+1][0] - 1:
                self.intervals[j][1] = self.intervals[j+1][1]
                self.intervals.pop(j+1)
                break
            elif val == self.intervals[j][0] - 1:
                self.intervals[j][0] -= 1
                break
            elif val == self.intervals[j][1] +1:
                self.intervals[j][1] += 1
                break
            elif val < self.intervals[j][0] - 1:
                self.intervals.insert(j, [val,val])
                break
            if j == N-1:
                self.intervals.append([val,val])


    def getIntervals(self):

        return self.intervals




if __name__ == '__main__':
    # solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    
    # Your SummaryRanges object will be instantiated and called as such:
    obj = SummaryRanges()
    # obj.addNum(6)
    # obj.addNum(6)
    obj.addNum(1)
    obj.addNum(3)
    param_1 = obj.getIntervals()
    output_Str = ' param_1 = ' + str(param_1)
    print(output_Str)
    
    obj.addNum(7)
    param_2 = obj.getIntervals()
    output_Str = ' param_2 = ' + str(param_2)
    print(output_Str)
    
    obj.addNum(2)
    param_3 = obj.getIntervals()
    output_Str = ' param_3 = ' + str(param_3)
    print(output_Str)
    
    obj.addNum(6)
    param_4 = obj.getIntervals()
    output_Str = ' param_4 = ' + str(param_4) 
    print(output_Str)