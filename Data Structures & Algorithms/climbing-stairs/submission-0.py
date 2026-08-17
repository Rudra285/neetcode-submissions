class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one = two = 1
        curr = 0

        for i in range(n - 1):
            curr = one + two
            two = one
            one = curr
        return curr

        