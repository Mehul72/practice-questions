class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix product array
        # postfix product array

        out, pre, post = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for i, n in enumerate(nums):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post[i] == 1
            else:
                post[i] = post[i + 1] * nums[i + 1]
        # print(pre)
        # print(post)

        for i in range(len(nums)):
            out[i] = pre[i] * post[i]
        # print(out)
        return out
            
        