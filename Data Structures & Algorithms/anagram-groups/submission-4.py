class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        checker = collections.defaultdict(list)

        for word in strs:
            key = [0] * 26
            for let in word:
                key[ord("a") - ord(let)] +=1
            checker[tuple(key)].append(word)

        return [vals for keys, vals in checker.items()]