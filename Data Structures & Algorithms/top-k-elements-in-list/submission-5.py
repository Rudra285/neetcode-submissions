import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = list()
        k_most = list()
        freq = dict()

        for i in nums:
            freq[i] = freq.get(i, 0) - 1

        for i in freq:
            heapq.heappush(pq, (freq[i], i))

        while k and pq:
            k_most.append(heapq.heappop(pq)[1])
            k -= 1
        
        return k_most