class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for i in nums:
            count[i] = count.get(i, 0) + 1
        sorted_freq_tup = sorted(count.items(), reverse=True, key= lambda x:x[1])

        sorted_freq = [i[0] for i in sorted_freq_tup]
        return sorted_freq[:k]