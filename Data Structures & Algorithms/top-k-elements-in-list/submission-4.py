class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        checker = {}
        freq = [[] for n in range(len(nums) + 1)]

        for n in nums:
            
            checker[n] = checker.get(n, 0) +1
        
        for n, c in checker.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)

        return res[:k]