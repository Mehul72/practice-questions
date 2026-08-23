class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add everything to a set.
        # go through nums in set, if n - 1 exists, skip, else keep track of max and current streak

        if not nums:
            return 0
        best = 1

        seen = set()

        for n in nums:
            seen.add(n)

        for n in nums:
            cur = 1
            if n - 1 in seen:
                continue
            i = n
            while i + 1 in seen:
                cur += 1
                i += 1
            best = max(best, cur)
        
        return best