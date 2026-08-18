class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r = 0, len(numbers) -1
        res = []

        while l < r:
            left = numbers[l]
            right = numbers[r]
            ans = left + right
            if ans == target:
                res.append(l+1)
                res.append(r+1)
                break
            elif ans > target:
                r -=1
                continue
            else:
                l +=1
                continue
        
        return res