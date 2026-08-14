class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = []

        left = 0
        right = k
        maxNum = max(nums[left:right])
        #num, index
        currentMax = [maxNum,nums[left:right].index(maxNum) + left]
        n.append(currentMax[0])

        while right<len(nums):
            left+=1
            right+=1
            
            #if max is out of the current window, find new max and update
            if(currentMax[1] < left):
                maxNum = max(nums[left:right])
                currentMax = [maxNum,left+ nums[left:right].index(maxNum)]

            #check if new element is greater than max, if it is update max
            if(nums[right-1] > currentMax[0]):
                currentMax[0] = nums[right-1]
                currentMax[1] = right-1
            
            n.append(currentMax[0])

        return n