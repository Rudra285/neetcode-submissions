import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while len(stones) > 1:
            k = len(stones) - 2
            temp = []
            while stones:
                temp.append(heapq.heappop(stones))
            if temp[-1] > temp[-2]:
                x = temp.pop()
                temp[-1] = x - temp[-1]
            elif temp[-2] == temp[-1]:
                temp.pop()
                temp.pop()
            for i in temp:
                heapq.heappush(stones, i)
        if stones:
            return heapq.heappop(stones)
        return 0