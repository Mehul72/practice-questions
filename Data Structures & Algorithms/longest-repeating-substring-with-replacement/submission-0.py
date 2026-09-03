class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hashmap l:n for things in current window
        # window length - count[most frequent] = no of things in the window needed replacements <= k

        count = {}
        res = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res





