# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        allList = []
        for i in range(0, len(pairs)):
            j = i
            while (j > 0 and pairs[j].key < pairs[j - 1].key):
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1
            allList.append(pairs.copy())
        return allList