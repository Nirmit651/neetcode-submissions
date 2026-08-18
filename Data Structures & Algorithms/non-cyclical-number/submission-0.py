class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
    
        while(n!=1):
            sumN = 0
            while(n>0):
                sumN+= (n%10) ** 2
                n = n//10
            if(sumN in seen):
                return False
            seen.add(sumN)
            n = sumN
        return True