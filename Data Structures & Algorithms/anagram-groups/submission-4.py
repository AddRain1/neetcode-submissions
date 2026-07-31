from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each string
        # for each 
        # use defaultdict
        map = defaultdict(list)
        for s in strs:
            counts = [0] * 26 # a ... z

            for c in s:
                counts[ord(c) - ord("a")] += 1

            map[tuple(counts)].append(s)

        return list(map.values())
