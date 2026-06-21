class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0 
        for num in nums:
            total += num
            prefix.append(total)
        total = 0 
        postfix = []
        for i in range(len(nums)-1,-1,-1):
            total += nums[i]
            postfix.append(total)
        postfix.reverse()
        l,r = 0, 0
        while l <= len(prefix)-1:
            if prefix[l] == postfix[r]:
                return l
            l+=1
            r+=1
        return -1
            

        
        
        