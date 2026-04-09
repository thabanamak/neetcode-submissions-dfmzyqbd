class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        count = 0
        array_length = len(nums)
        majority = array_length//2
        for x in range(array_length):
            if nums[x] == target:
                count +=1 
                if count > majority:
                    return True
                continue
            else:
                continue
       
        return False

            
            
        