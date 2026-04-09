class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        n = len(nums)
        left, right = 0, n - 1
        first_index = n 

        while left <= right: 
            mid = (left+right)//2
            if nums[mid] >= target:
                first_index = mid 
                right = mid - 1 
            else:
                left = mid + 1

        check_index = first_index + n // 2
        return check_index < n and nums[check_index] == target
            
            
        