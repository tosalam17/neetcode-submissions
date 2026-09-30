class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_key = [0] * 26
        t_key = [0] * 26
        if len(s) != len(t):
            return False
        

        for letter in s:
            s_key[ord("a") - ord(letter)] +=1

        for letter in t:
            t_key[ord("a") - ord(letter)] +=1
        return s_key == t_key

        