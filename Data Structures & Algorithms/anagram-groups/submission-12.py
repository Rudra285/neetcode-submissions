class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = dict()

        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in grouped:
                grouped[sorted_word] = [word]
            else:
                grouped[sorted_word].append(word)

        return list(grouped.values())