class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        output = [1] * len(nums)

        # One pass with prefix 
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        # One pass with the postfix multiplying the numbers from the prefix pass
        # This starts from the back of the array and goes backwards
        for i in range(len(nums) - 1, -1 , -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output 
        