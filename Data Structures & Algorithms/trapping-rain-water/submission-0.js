class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let minLR = []
        let minL = []
        let minR = []

        let maxLeft = 0;
        for(let i = 0;i<=height.length;i++) {
            minL[i] = maxLeft;
            if(height[i]>maxLeft) {
                maxLeft=height[i]
            }      
        }

        let maxRight = 0;
        for(let i = height.length-1;i>=0;i--) {
            minR[i] = maxRight;
            if(height[i]>maxRight) {
                maxRight=height[i]
            }      
        }

        for(let i = height.length-1;i>=0;i--) {
            minLR[i] = Math.min(minL[i], minR[i])
        }

        console.log(minL)
        console.log(minR)
        console.log(minLR)

        let totalWater = 0;
        for(let i = 0;i<=height.length;i++) {
            let water = minLR[i] - height[i]
            if(water>0) {
                totalWater+=water;
            }
        }

        return totalWater;
    }
}
