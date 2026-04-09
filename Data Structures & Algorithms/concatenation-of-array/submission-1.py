class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        for x in nums:
            arr.append(x)
        for x in nums:
            arr.append(x)
        return arr      