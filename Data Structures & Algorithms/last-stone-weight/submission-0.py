class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-n for n in stones]
        heapq.heapify(stoneHeap)
        
        while(len(stoneHeap) > 1):
            x = -heapq.heappop(stoneHeap)
            y = -heapq.heappop(stoneHeap)

            if x==y:
                continue;
            elif x>y:
                newStone = x-y
                heapq.heappush(stoneHeap, -newStone)
            else:
                newStone = y-x
                heapq.heappush(stoneHeap, -newStone)

        return -stoneHeap[0] if stoneHeap else 0