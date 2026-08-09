class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sortedTuples = sorted(count.items(), key=lambda x:x[1])

        arr = []

        for i in range(len(sortedTuples) - k, len(sortedTuples)):
            arr.append(sortedTuples[i][0])

        return arr
        
