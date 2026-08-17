import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        popped_val = []
        heapq.heappush(self.nums, val)
        largest_k = len(self.nums) - self.k
        for i in range(largest_k):
            popped_val.append(heapq.heappop(self.nums))
        k_val = heapq.heappop(self.nums)
        heapq.heappush(self.nums, k_val)
        while popped_val:
            heapq.heappush(self.nums,popped_val.pop())
        return k_val