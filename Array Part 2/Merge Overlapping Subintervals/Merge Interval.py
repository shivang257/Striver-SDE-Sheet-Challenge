class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out=[intervals[0]]
        for i,j in intervals[1:]:
            last=out[-1][1]
            if i<=last:
                out[-1][1]=max(out[-1][1],j)
            else:
                out.append([i,j])
        return out
    