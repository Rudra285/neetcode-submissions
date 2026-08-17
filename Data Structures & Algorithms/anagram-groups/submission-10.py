class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        grouped = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s not in grouped:
                grouped[s] = [i]
            else:
                grouped[s].append(i)
        return list(grouped.values())
