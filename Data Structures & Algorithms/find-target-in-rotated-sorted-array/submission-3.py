class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = 0

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        if nums[pivot] <= target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif(target > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
            
