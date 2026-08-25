class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = (r - l) * min(heights[l], heights[r])
        # try a greedy approach first, start with widest container
        # move left and right depending on whichever on is smaller

        l, r = 0, len(heights) - 1
        best = 0
        
        while l < r:
            cur = (r - l) * min(heights[l], heights[r])
            best = max(best, cur)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best