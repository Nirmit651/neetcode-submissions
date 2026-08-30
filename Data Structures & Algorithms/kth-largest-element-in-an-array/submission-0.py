class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]

        heapq.heapify(maxHeap)

        kLargest = 0;
        for i in range(0,k):
            kLargest = -heapq.heappop(maxHeap)

        return kLargest
