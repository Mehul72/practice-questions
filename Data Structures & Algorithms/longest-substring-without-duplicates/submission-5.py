class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # look at one flexible window and keep track of what has been
        # seen so for in that window and keep count of max

        if not s:
            return 0
        seen = set()
        best = 1
        l = 0

        seen.add(s[l])

        for r in range(1, len(s)):
            while s[r] in seen:

                seen.remove(s[l])
                l += 1
    

            seen.add(s[r])

            best = max(best, r - l + 1)

        return best

        