class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = dict()
        s2_count = dict()
        left = 0
        right = 0
        looking = False
        for i in s1:
            s1_count[i] = s1_count.get(i, 0) + 1
        for i in range(len(s2)):
            if s2[i] not in s1_count:
                if s2[i - 1] in s1_count:
                    s2_count = dict()
                left = right = i + 1
            else:
                looking = True
                s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
                right += 1
                if s2_count == s1_count:
                    print(s2[left:right + 1])
                    return True
                while s2_count[s2[i]] > s1_count[s2[i]] and right - left != 0:
                    s2_count[s2[left]] -= 1
                    left += 1
        return False
                