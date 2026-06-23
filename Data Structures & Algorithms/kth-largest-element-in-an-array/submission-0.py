import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        val = 0 
        while k:
            val = heapq.heappop(nums)
            k-=1
        return -val
        