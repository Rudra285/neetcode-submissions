class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2::]
        rev_bin = '0b' + binary[::-1]
        rem = 32 - len(binary)
        return int(rev_bin + '0' * rem, 2)