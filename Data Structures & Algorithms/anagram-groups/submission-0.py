class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        overall = defaultdict(list)

        for word in strs:
            counter = [0] * 26

            for l in word:
                counter[ord(l) - ord("a")] +=1

            overall[tuple(counter)].append(word)
        
        return list(overall.values())