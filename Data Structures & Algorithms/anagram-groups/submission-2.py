class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        checker = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                key[index] +=1
            checker[tuple(key)].append(word)

                
        return [anagrams for anagrams in checker.values()]
            
