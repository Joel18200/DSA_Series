class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merge=[]
        prev=intervals[0]
        for i in range(1,len(intervals)):
            if prev[1]>=intervals[i][0]:
                prev[1]=max(prev[1],intervals[i][1])
            else:
                merge.append(prev)
                prev=intervals[i]
        else:
            merge.append(prev)
        return merge