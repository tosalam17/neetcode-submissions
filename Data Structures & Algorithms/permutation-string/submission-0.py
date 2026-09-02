class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = {}
        s2count = {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1count[s1[i]] = s1count.get(s1[i], 0) +1
            s2count[s2[i]] = s2count.get(s2[i], 0) +1
        if s2count == s1count:
            return True
        
        for r in range(len(s1), len(s2)):
            s2count[s2[r]] = s2count.get(s2[r], 0) +1
            
            left = s2[r-len(s1)]
            s2count[left] -=1
            if s2count[left] == 0:
                del s2count[left]
            
            if s2count == s1count:
                return True
        
        return False

            
        
        


            


        
        