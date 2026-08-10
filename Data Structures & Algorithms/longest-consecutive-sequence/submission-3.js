class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let numSet = new Set(nums);
        let longest = 0;

        nums.forEach(num => {
            if(!numSet.has(num-1)) {
                let length = 1;
                while(numSet.has(num+1)) {
                    num=num+1;
                    length++;
                }
                longest = Math.max(longest, length)
            }
        })

        return longest;
    }
}
