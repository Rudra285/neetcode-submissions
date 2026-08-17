class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        unique = []

        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        
        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])
        
        for num, count in counter.items():
            buckets[count].append(num)
        print(buckets)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                unique.append(num)
                if len(unique) == k:
                    return unique