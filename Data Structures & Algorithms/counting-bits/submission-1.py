class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            bin_sum = 0
            binary = bin(i)[2:]
            for b in binary:
                bin_sum += int(b)
            output.append(bin_sum)
        return output