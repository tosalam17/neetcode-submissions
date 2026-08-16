class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        checker = collections.defaultdict(list)

        for word in strs:
            key = [0] * 26
            for l in word:
                key[ord(l) - ord('a')] +=1

            checker[tuple(key)].append(word)

        return [anagram for anagram in checker.values()] 