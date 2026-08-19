class Solution {
    /**
     * @param {number[][]} matrix
     * @return {void}
     */
    rotate(matrix) {
        
        //make rows into cols
        for(let i = 0;i < matrix.length;i++) {

            for(let j = i + 1;j < matrix[i].length;j++) {
                //i = 0, j = 1
                let temp = matrix[j][i]
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = temp 
            }
        }

        //reverse the cols by reversing the rows
        for(let i = 0;i < matrix.length;i++) {
            let left = 0
            let right = matrix[i].length - 1
            while(left<=right) {
                let temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left++
                right--
            }
        }


        return matrix
        
    }
}
