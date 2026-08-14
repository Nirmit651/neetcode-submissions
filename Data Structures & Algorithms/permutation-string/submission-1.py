class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = {}

        # get counts for s1
        for r in range(len(s1)):
            countS1[s1[r]] = countS1.get(s1[r], 0) + 1

        l = 0
        r = len(s1)
        countWindow = {}

        # build first window
        for j in range(l, r):
            countWindow[s2[j]] = countWindow.get(s2[j], 0) + 1

        while r <= len(s2):
            if countWindow == countS1:
                return True

            # can't slide any farther
            if r == len(s2):
                break

            # remove left char
            countWindow[s2[l]] -= 1

            if countWindow[s2[l]] == 0:
                del countWindow[s2[l]]

            # add new right char
            countWindow[s2[r]] = countWindow.get(s2[r], 0) + 1

            l += 1
            r += 1

        return False