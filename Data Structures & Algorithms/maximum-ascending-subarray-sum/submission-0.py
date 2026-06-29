class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum = nums[0]
        current_sum = nums[0]
        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                current_sum += nums[r]
            else:
                current_sum = nums[r]
            maxsum = max(maxsum, current_sum)
        return maxsum
        