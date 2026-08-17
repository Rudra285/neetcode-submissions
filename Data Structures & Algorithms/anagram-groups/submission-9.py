class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_sorter = {}
        results = []
        sorted_anagrams = strs.copy()
        for i in range(len(sorted_anagrams)):
            sorted_anagrams[i] = "".join(sorted(sorted_anagrams[i]))
        
        for i, e in enumerate(sorted_anagrams):
            if e not in anagram_sorter:
                anagram_sorter[e] = []
            anagram_sorter[e].append(i)
        
        for l in anagram_sorter.values():
            new_list = []
            for i in l:
                new_list.append(strs[i])
            results.append(new_list)
                
        return results
