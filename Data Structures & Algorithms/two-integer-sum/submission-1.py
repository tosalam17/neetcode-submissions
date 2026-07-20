class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        mymap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mymap:
                return [mymap[comp],i]
            else:
                mymap[nums[i]] = i
        
        return []