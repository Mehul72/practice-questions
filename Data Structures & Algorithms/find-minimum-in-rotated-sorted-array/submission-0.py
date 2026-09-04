class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search

        # N N N N N S S S
        # 7 8 9
        # find the first S
        # first elemet of sorted
        # comapre middle with rightmost. if sorted then its in left if not its in right

        l, r = 0, len(nums) - 1

        while l < r:
            m = (r + l) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]


