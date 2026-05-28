class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0 
        hashset = set(nums)

        for num in hashset:
            if (num-1) not in hashset:
                length = 1 
                while (num + length) in hashset:
                    length += 1 
                count = max(length, count)
        return count
        