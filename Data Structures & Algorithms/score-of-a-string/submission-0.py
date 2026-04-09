class Solution:
    def scoreOfString(self, s: str) -> int:
        arr = []
        for i in range(len(s)-1):
            x = abs(ord(s[i]) - ord(s[i+1]))
            arr.append(x)
        total = sum(arr)
        return total
        