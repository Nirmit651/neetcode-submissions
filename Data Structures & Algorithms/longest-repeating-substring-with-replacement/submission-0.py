class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        for r in range(len(s)):
            #add char to the hash map
            count[s[r]] = 1 + count.get(s[r],0)

            while (r - left + 1) - max(count.values()) > k:
                #decrement the frequency of char at left since we're removing
                # it from the window
                count[s[left]] -= 1
                #move window
                left+=1

            #keep the max valid window length
            res = max(res, r - left +1)
        return res
        