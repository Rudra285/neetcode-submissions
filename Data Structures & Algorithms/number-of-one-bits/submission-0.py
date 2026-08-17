class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        res = 0
        for i in n:
            if i == '1':
                res += int(i)
        return res