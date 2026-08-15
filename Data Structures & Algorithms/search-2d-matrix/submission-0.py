class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if(target == matrix[i][0] or target == matrix[i][len(matrix[i])-1]):
                return True
            if target > matrix[i][0] and target < matrix[i][len(matrix[i])-1]:
                arr = matrix[i]
                left = 0
                right = len(matrix[i]) - 1

                while(left<=right):
                    mid = ((right-left) // 2) + left

                    if(arr[mid] == target):
                        return True
                    elif(arr[mid] > target):
                        right = mid - 1
                    elif(arr[mid] < target):
                        left = mid + 1
        return False
                