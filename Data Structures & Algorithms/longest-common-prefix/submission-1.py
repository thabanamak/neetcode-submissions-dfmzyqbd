class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        for s in strs:
            min_len = min(min_len, len(s))

        res = ""
        for i in range(min_len):
            same = True 
            for j in range(len(strs)):
                if strs[0][i] != strs[j][i]: same = False

            if same:
                res += strs[0][i]
            else:
                break

        return res



        