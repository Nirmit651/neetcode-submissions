class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        differences = {};
        
        for i, n in enumerate(nums):
            d = target-nums[i];
            if d in differences:
                return [differences[d], i]
            differences[n] = i
            
            
