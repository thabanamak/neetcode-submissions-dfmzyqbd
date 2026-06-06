class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sum_sq = 0
            temp = n
            while temp:
                digit = temp % 10
                sum_sq += digit * digit
                temp //= 10
            n = sum_sq
        return True
        