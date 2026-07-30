class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        check = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            check[n] = 1 + check.get(n, 0)
        for n, c in check.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
        return res[:k] 
        
        