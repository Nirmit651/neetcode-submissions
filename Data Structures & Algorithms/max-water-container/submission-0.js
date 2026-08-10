class Solution {
    /*** @param {number[]} 
     * heights* 
     * @return {number}*/
    maxArea(heights) {
        let right = heights.length-1;
        let left = 0;
        let max = 0;

        while(left<=right) {
            const height = Math.min(heights[left], heights[right]);
            const width = right - left;
            const currentArea = height * width;

            max = Math.max(max, currentArea);

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return max;

    }

}