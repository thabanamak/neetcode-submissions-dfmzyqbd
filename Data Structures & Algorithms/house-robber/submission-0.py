class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        first, second = 0, 0 
        for num in nums:
            temp = max(num + first, second)
            first = second
            second = temp

        return second

        
        