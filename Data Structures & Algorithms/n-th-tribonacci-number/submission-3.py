class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 0:
            return -1
        if n == 0:
            return 0
        if n <= 2:
            return 1
        first = 0 
        second = 1 
        third = 1

        res = float('inf')
        for i in range(3,n+1):
            res = first + second + third
            first = second 
            second = third
            third = res

        return res
        