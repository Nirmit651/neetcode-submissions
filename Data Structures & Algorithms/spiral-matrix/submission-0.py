class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        s = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            #top row
            for i in range(left, right+1):
                s.append(matrix[top][i])
            top+=1

            #right col
            for i in range(top, bottom+1):
                s.append(matrix[i][right])
            right-=1

            #bottom row
            if top <= bottom:
                for i in range(right, left - 1,-1):
                    s.append(matrix[bottom][i])
                bottom-=1

            #left col
            if left <= right:
                for i in range(bottom, top-1, -1):
                    s.append(matrix[i][left])
                left+=1

        return s