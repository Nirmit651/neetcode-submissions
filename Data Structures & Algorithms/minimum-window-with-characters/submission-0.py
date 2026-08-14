class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}

        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1

        countWindow = {}
        result = ""
        
        l = 0
        need = len(countT)
        have = 0

        for r in range(len(s)):
            countWindow[s[r]] = countWindow.get(s[r], 0) + 1
            
            if(s[r] in countT and countWindow[s[r]] == countT[s[r]]):
                have+=1

            while(need==have):

                if(result == "" or len(s[l:r+1]) < len(result)):
                    result = s[l:r+1] 
                
                
                if s[l] in countT:
                    countWindow[s[l]] -= 1

                    if countWindow[s[l]] < countT[s[l]]:
                        have -= 1

                l+=1

        return result

        
        