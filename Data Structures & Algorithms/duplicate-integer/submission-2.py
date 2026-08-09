class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        originalLength = len(nums)
        hashSet = set(nums)
        if originalLength > len(hashSet):
            return True
        return False
