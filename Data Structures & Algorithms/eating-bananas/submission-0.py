class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        minK =  max(piles)
        left = 1
        right = max(piles)

        while(left<=right):
            currentK = left + ((right-left) // 2)
            currentH = 0
            for pile in piles:
                currentH += math.ceil(pile/currentK)
            
            if(currentH > h):
                left = currentK + 1
            elif (currentH <= h):
                right = currentK - 1 
                minK = min(minK, currentK)


        return minK