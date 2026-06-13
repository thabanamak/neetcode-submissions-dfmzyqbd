class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n, m = len(word1), len(word2)
        for x in range(max(n,m)):
            if x < n:
                res.append(word1[x])
            if x < m:
                res.append(word2[x])
        return "".join(res)

        