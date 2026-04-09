class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        for x in nums:
            candidate = nums[0]
            if x == candidate:
                count +=1
            else:
                count -=1
            if count < 1:
                candidate = x
            
        return candidate
        