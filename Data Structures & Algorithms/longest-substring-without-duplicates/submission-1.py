class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        longest = 0
        seenset = set()
        for j in range(len(s)):
            while s[j] in seenset:
                seenset.remove(s[i])
                i+=1
            
            seenset.add(s[j])

            longest = max(longest, j-i +1)

        return longest

        