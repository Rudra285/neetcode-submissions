class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        nums.sort()
        unique = []

        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        counter = dict(sorted(counter.items(), key=lambda item : item[1], reverse=True))
        
        i = e = 0
        while i < k:
            if list(counter.keys())[e] not in unique:
                unique.append(list(counter.keys())[e])
                i += 1
            e += 1
        
        unique.sort()
        return unique