class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)[2:]
        bin_sum = 0
        for i in bin_n:
            bin_sum += int(i)
        return bin_sum