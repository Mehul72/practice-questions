class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # have 2 pointers. start and end. move in or out depending on how far off you are.

        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
                l += 1
        
        return -1
        