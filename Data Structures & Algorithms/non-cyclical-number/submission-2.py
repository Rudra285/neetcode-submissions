class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cycle_sum = None
        while cycle_sum != 1:
            cycle_sum = 0
            strn = str(n)
            for i in strn:
                cycle_sum += int(i) ** 2
            if cycle_sum in seen:
                return False
            seen.add(cycle_sum)
            n = str(cycle_sum)
        return True