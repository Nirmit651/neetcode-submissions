class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let middle = 0;
        let right = nums.length-1;
        let triplets = [];

        nums.sort((a, b) => a - b);

        for(let i = 0;i<nums.length-1;i++) {
            middle = i + 1;
            right = nums.length-1;
            if (i > 0 && nums[i] === nums[i - 1]) continue;

            while(middle<right) {           
                if(nums[middle]+nums[right]==-nums[i]) {
                    triplets.push([nums[i], nums[middle], nums[right]]);
                    middle++;
                    right--;

                    while (middle < right && nums[middle] === nums[middle - 1]) {
                        middle++;
                    }

                    while (middle < right && nums[right] === nums[right + 1]) {
                        right--;
                    }
                } else if(nums[middle]+nums[right]>=-nums[i]) {
                    right--;
                } else {
                    middle++;
                }
            }
        }

        return triplets;
        
    }
}
