class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in counter:
                counter[n] +=1
            else:
                counter[n] = 1
        
        for n, c in counter.items():
            freq[c].append(n)
        out = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                out.append(n)
                if len(out) == k:
                    return out

