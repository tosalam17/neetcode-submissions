class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l , r = 0, len(heights) -1
        res = 0

        while l <= r:
            height = min(heights[l], heights[r])
            width = r - l
            area = height * width
            if area < res:
                if heights[l] < heights[r]:
                    l +=1
                elif heights[l] > heights[r]:
                    r -=1
                else:
                    l +=1
            else:
                res = area
                if heights[l] > heights[r]:
                    r -=1
                else:
                    l +=1
        
        return res

        