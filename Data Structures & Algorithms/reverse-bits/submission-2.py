class Solution:
    def reverseBits(self, n: int) -> int:
        rem = 34 - len(bin(n))
        rev = ''
        for i in range(len(bin(n)) - 1, 1, -1):
            rev += bin(n)[i]
        for i in range(rem):
            rev += '0'
        return int(rev, 2)