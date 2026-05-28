class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0 
        hashset = set(nums)

        for i in hashset:
            if (i - 1) not in hashset:
                length = 1
                while (i + length) in hashset:
                    length += 1
                count = max(count, length)
        
        return count