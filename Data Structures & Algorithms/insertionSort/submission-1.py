# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []

        for x in range(n):
            i = x-1

            while i >= 0 and pairs[i+1].key < pairs[i].key:
                tmp = pairs[i+1]
                pairs[i+1] = pairs[i]
                pairs[i]  = tmp
                i-=1

            res.append(pairs[:])

        return res
        