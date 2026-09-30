class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in check:
                return [check[comp], i]
            else:
                check[num] = i
        
