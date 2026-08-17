class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n + 1):
            total = 0
            while i:
                if i % 2 == 1:
                    total += 1
                i = i // 2
            bits.append(total)
        
        return bits
        


