class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        ints = []
        currentInt = intervals[0]

        for i in range (1, len(intervals)):
            if intervals[i][0] <= currentInt[1]:
                if intervals[i][1] > currentInt[1]:
                    currentInt[1] = intervals[i][1]
            else:
                ints.append(currentInt)
                currentInt = intervals[i]
        ints.append(currentInt)
        return ints