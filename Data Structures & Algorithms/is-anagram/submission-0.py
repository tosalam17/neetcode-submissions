class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scheck = {}
        tcheck = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in scheck:
                scheck[s[i]] +=1
            else:
                scheck[s[i]] = 1
            if t[i] in tcheck:
                tcheck[t[i]] +=1
            else:
                tcheck[t[i]] = 1

        return (scheck == tcheck)
