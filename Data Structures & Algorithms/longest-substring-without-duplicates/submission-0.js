class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let left = 0;
        let maxLength = 0;
        let seenChars = new Set()

        for(let right = 0;right<s.length;right++){

            while(seenChars.has(s[right])) {
                seenChars.delete(s[left]);
                left++;
            }

            seenChars.add(s[right]);
            maxLength = Math.max(maxLength, right-left+1);
        }

        return maxLength;
    }
}
